from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_driver(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            return redirect('driver_dashboard')
        else:
            pass
    return render(request, 'driver/login.html')