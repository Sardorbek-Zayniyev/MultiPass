from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from auth_providers.email_password_auth.models import Profile
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation


@login_required(login_url='account_login')
def profile(request):

    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        enable_otp = request.POST.get('otp_toggle') == 'on'

        if enable_otp and not request.session.get('otp_in_progress', False):
            # Mark OTP setup in progress
            request.session['otp_in_progress'] = True
            messages.info(
                request, "OTP sent. Please confirm to enable two-step verification.")
            # Redirect to OTP verification page
            return redirect('generate_email_otp')
        elif not enable_otp:
            # Disable OTP immediately
            profile.otp_enabled = False
            profile.save()
            messages.info(request, "Two-step verification disabled.")

        user_form = UserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('profile')
    else:
        user_form = UserChangeForm(instance=request.user)
    context = {
        'user_form': user_form,
    }
    return render(request, "profile.html", context)


@login_required
def redirect_after_login(request):
    try:
        if request.user.profile.otp_enabled:
            return redirect('generate_email_otp')
    except Exception as e:
        pass
    return redirect('profile')
