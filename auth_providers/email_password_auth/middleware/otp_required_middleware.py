from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User


class OTPRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.user.is_authenticated
            and not request.path.startswith('/admin/')  # Allow admin access
            and '/admin/' not in request.path
            and hasattr(request.user, 'profile')  # Ensure profile exists
            and request.user.profile.otp_enabled  # Ensure OTP is enabled
            # OTP setup in progress
            and request.session.get('otp_in_progress', False)
            and request.path not in [reverse('verify_email_otp'), reverse('generate_email_otp')]
        ):
            return redirect('verify_email_otp')

        return self.get_response(request)
