# from django.shortcuts import render, redirect
# from django.contrib.auth import get_user_model
# from django.contrib.auth.decorators import user_passes_test

# User = get_user_model()

# @user_passes_test(lambda u: u.is_staff)
# def register_driver(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         phone_number = request.POST['phone_number']
#         driver_license = request.POST['driver_license']
#         email = request.POST['email']
#         password = request.POST['password']

#         user = User.objects.create_user(
#             first_name=first_name,
#             last_name=last_name,
#             phone_number=phone_number,
#             driver_license=driver_license,
#             email=email,
#             password=password
#         )
#         return redirect('success_page')
#     else:
#         return render(request, 'driver/register.html')

from rest_framework import status
from rest_framework.response import Response

# views.py
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import UserSerializer


class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
