from django.db import models
from django.contrib.auth.models import AbstractUser
from forwarding.models import Info_transport
from staff.models import Truck, Trailer


DRIVE_LICENSE = [
        ('C', 'C'),
        ('C+E', 'C+E'),
    ]


STATUS_CHOICES = [
    ("on_site", "Na miejscu"),
]


STATUS_SERVICES = [
    ("Yes", "Przesmarowany"),
    ("No", "Nie przesmarowany")
]

STATUS_FUEL = [
    ("Yes", "Zatankowany"),
    ("No", "Nie zatankowany")
]


LOADING_STATUS_CHOICES = [
        ('loaded', 'Załadowany'),
        ('waiting_for_loading', 'Oczekiwanie na załadunek'),
    ]


UNLOADING_STATUS_CHOICES = [
        ('unloaded', 'Rozładowany'),
        ('waiting_for_unloading', 'Oczekiwanie na rozładunek'),
    ]


class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True, verbose_name="Imię")
    last_name = models.CharField(max_length=30, blank=True, verbose_name="Nazwisko")
    phone_number = models.CharField(max_length=10, unique=True, blank=True, verbose_name="Numer telefonu")
    drive_license = models.CharField(choices=DRIVE_LICENSE, blank=True, verbose_name="Prawo jazdy")
    email_address = models.EmailField(unique=True, blank=True, verbose_name="Email") 
    
    # def __str__(self):
    #     return self.firs_name + self.last_name


class Info_of_truck(models.Model):
    driver_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Kierowca")
    truck_number = models.ForeignKey(Truck, on_delete=models.SET_NULL, null=True, verbose_name="Rejestracja ciężarówki")
    trailer_number = models.ForeignKey(Trailer, on_delete=models.SET_NULL, null=True, verbose_name="Rejestracja przyczepy")
    mileage = models.DecimalField(max_digits=8, decimal_places=1, verbose_name="Przebieg", blank=True)
    fuel = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Tankowanie", blank=True)
    service = models.CharField(choices=STATUS_SERVICES, verbose_name="Serwis")
    description = models.TextField(verbose_name="Uwagi")


class Status_of_load(models.Model):
    loading_status = models.CharField(choices=LOADING_STATUS_CHOICES)
    unloading_status = models.CharField(choices=UNLOADING_STATUS_CHOICES)
    
class Load_info(models.Model):
    load_info = models.OneToOneField(Info_transport, on_delete=models.CASCADE)