from firebase_admin import auth
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def phone_number_login(request):
    return render(request, 'phone_number.html')


def send_otp(request):
    """
    Sends OTP to the user's phone number via Firebase
    """
    phone_number = request.GET.get('phone')
    if not phone_number:
        return JsonResponse({"error": "Phone number is required"}, status=400)

    try:
        # Simulating OTP send (handled by Firebase on the frontend)
        auth.create_user(phone_number=phone_number)
        return JsonResponse({"success": "OTP sent to phone number"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def verify_otp(request):
    """
    Verifies the OTP and authenticates the user
    """
    phone_number = request.GET.get('phone')
    otp = request.GET.get('otp')
    if not phone_number or not otp:
        return JsonResponse({"error": "Phone number and OTP are required"}, status=400)

    try:
        # Normally, OTP verification happens on the frontend
        user = auth.get_user_by_phone_number(phone_number)
        return JsonResponse({"success": "User verified", "user_id": user.uid})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
