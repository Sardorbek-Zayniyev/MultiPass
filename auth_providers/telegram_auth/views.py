from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from auth_providers.email_password_auth.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login
from telegram import Bot
from datetime import datetime
import hmac
import hashlib
from decouple import config

TELEGRAM_BOT_API_TOKEN = config('TELEGRAM_BOT_API_TOKEN')
bot = Bot(token=TELEGRAM_BOT_API_TOKEN)  # Initialize Telegram Bot


def telegram_callback(request):
    if request.method != 'GET':
        return HttpResponseBadRequest("Invalid request")

    data = request.GET
    required_keys = {"id", "first_name", "last_name", "username", "hash"}

    # Check if all required keys are present
    if not required_keys.issubset(data.keys()):
        return HttpResponseBadRequest("Missing parameters")

    # Validate hash
    data_check_string = "\n".join(
        f"{k}={data[k]}" for k in sorted(data) if k != "hash"
    )
    secret_key = TELEGRAM_BOT_API_TOKEN.encode('utf-8')
    calculated_hash = hmac.new(secret_key, data_check_string.encode(
        'utf-8'), hashlib.sha256).hexdigest()

    if calculated_hash != data["hash"]:
        return HttpResponseBadRequest("Invalid hash")

    # Extract user data
    telegram_id = int(data["id"])
    first_name = data.get("first_name", "")
    last_name = data.get("last_name", "")
    username = data.get("username") or str(telegram_id)

    # Fetch user profile photo
    try:
        user_photos = bot.get_user_profile_photos(user_id=telegram_id, limit=1)
        photo_url = user_photos.photos[0][0].file_id if user_photos.total_count > 0 else None
    except Exception:
        photo_url = None

    # Get or create user and profile
    try:
        profile = Profile.objects.get(telegram_id=telegram_id)
        user = profile.user

        # Update profile fields if necessary
        profile.telegram_username = username
        profile.photo_url = photo_url
        profile.auth_date = datetime.now()
        profile.save()

    except Profile.DoesNotExist:
        user, created = User.objects.get_or_create(
            username=username, defaults={
                "first_name": first_name, "last_name": last_name}
        )
        if created:
            Profile.objects.create(
                user=user,
                telegram_id=telegram_id,
                telegram_username=username,
                photo_url=photo_url,
                auth_date=datetime.now()
            )

    # Log the user in
    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('profile')
