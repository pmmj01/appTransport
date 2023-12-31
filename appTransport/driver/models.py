from django.db import models
from django.contrib.auth.models import User
from forwarding.models import Info_transport
from staff.models import Truck, Trailer


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