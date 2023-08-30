from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .models import User
from utils import generate_confirmation_token, send_confirmation_email


def login_email(request):
    email = request.POST.get('email')
    confirmation_token = generate_confirmation_token()
    user = User.objects.filter(email=email, confirmation_token=confirmation_token).first()
    if user:
        user = authenticate(request, username=user.username, password=None)
        login(request, user)
        return redirect('index')
    else:
        send_confirmation_email(email, confirmation_token)
        return redirect('confirmation')

