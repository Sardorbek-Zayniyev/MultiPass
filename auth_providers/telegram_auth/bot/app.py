import logging
import os
from telegram.constants import ParseMode
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import urllib.parse
import hashlib
import hmac

# Use environment variables for sensitive data
TELEGRAM_BOT_API_TOKEN = os.environ.get('TELEGRAM_BOT_API_TOKEN')
DJANGO_CALLBACK_URL = "http://127.0.0.1:8000/accounts/telegram/callback/"

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        start_parameter = context.args[0]
        if start_parameter == "auth":
            user = update.effective_user
            if not user:
                logger.warning("User object is None. Update: %s", update)
                return

            # Fetch user profile photos
            try:
                user_photos = await context.bot.get_user_profile_photos(user_id=user.id, limit=1)
                photo_url = user_photos.photos[0][0].file_id if user_photos.total_count > 0 else None
            except Exception as e:
                logger.error(f"Failed to fetch user profile photos: {e}")
                photo_url = None
            logger.info(f"Photo URL: {photo_url}")

            # Prepare user data
            username = user.username if user.username is not None else str(
                user.id) + user.first_name
            user_data = {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name or "",
                "photo_url": photo_url,
                "username": username
            }

            # Generate hash for validation
            data_check_string = "\n".join(
                f"{k}={user_data[k]}" for k in sorted(user_data))
            secret_key = TELEGRAM_BOT_API_TOKEN.encode('utf-8')
            message = data_check_string.encode('utf-8')
            calculated_hash = hmac.new(
                secret_key, message, hashlib.sha256).hexdigest()
            user_data["hash"] = calculated_hash

            # Build redirect URL
            encoded_params = urllib.parse.urlencode(user_data)
            redirect_url = f"{DJANGO_CALLBACK_URL}?{encoded_params}"

            # Send the message with the login link
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Please click this link to complete login: <a href='{
                    redirect_url}'>Login</a>",
                parse_mode=ParseMode.HTML,
            )
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid auth parameter")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the bot!")


def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_API_TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
