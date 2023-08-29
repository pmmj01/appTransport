from django.urls import path
from . import views

app_name = 'driver'


urlpatterns = [
    path('register/', views.register_driver, name='register_driver'),
]