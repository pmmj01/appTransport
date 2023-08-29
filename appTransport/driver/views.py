from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test

User = get_user_model()

@user_passes_test(lambda u: u.is_staff)
def register_driver(request):
    if request.method == 'POST':
        pass
    else:
        pass
    
    return render(request, 'driver/register.html')