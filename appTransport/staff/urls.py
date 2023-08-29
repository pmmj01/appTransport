from django.urls import path
from . import views

app_name = 'staff'


urlpatterns = [
    path('login/', views.login_driver, name='login_driver'),
]