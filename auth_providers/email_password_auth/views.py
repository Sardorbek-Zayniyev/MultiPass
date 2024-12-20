from django_otp.plugins.otp_email.models import EmailDevice
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def generate_email_otp(request):

    if request.session.get('otp_verified'):
        return redirect('profile')

    user = request.user
    device, created = EmailDevice.objects.get_or_create(
        user=user, name=user.username)  # Create or get EmailDevice
    device.generate_challenge()  # Generates OTP and sends email
    messages.info(request, "An OTP has been sent to your email.")
    return redirect('verify_email_otp')


@login_required
def verify_email_otp(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        otp_code = request.POST.get('otp')
        device = EmailDevice.objects.filter(
            user=request.user, name=user.username).first()

        if device and device.verify_token(otp_code):
            profile.otp_enabled = True  # Enable two-step verification
            profile.save()
            # Clear OTP setup flag
            request.session.pop('otp_in_progress', None)
            messages.success(request, 'OTP verified successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid or expired OTP. Try again.')
    return render(request, 'account/confirm_login_code.html', {'user': user})
