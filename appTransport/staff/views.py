from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


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


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user and user.is_staff:
            login(request, user)
            return JsonResponse({'message': 'Zalogowano jako admin'}, status=200)
        else:
            return JsonResponse({'message': 'Błąd logowania'}, status=401)
    return JsonResponse({'message': 'Metoda nieobsługiwana'}, status=405)


class DataAPIView(APIView):
    def get(self, request):
        data = {"message": "Hello from Django API!"}
        return Response(data)
    
    
