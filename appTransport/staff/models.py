from django.db import models

TYPE = [("standard", "Standard"), ("mega", "Mega")]


class Truck(models.Model):
    truckRegistration = models.CharField(
        max_length=8, blank=True, unique=True, verbose_name="Numer rejestracyjny"
    )
    truckNumber = models.CharField(
        max_length=3, blank=True, unique=True, verbose_name="Numer boczny"
    )
    truckType = models.CharField(choices=TYPE, blank=True, verbose_name="Rodzaj auta")
    truckFuelTank = models.CharField(
        max_length=4, blank=True, verbose_name="Zbiornik paliwa"
    )
    truckHP = models.CharField(max_length=3, blank=True, verbose_name="Moc")


class Trailer(models.Model):
    trailerRegistration = models.CharField(
        max_length=8, blank=True, unique=True, verbose_name="Numer rejestracyjny"
    )
    trailerNumber = models.CharField(
        max_length=3, blank=True, unique=True, verbose_name="Numer boczny"
    )
    trailerType = models.CharField(
        choices=TYPE, blank=True, verbose_name="Rodzaj naczepy"
    )


class WorkerDriver(models.Model):
    name = models.CharField(max_length=32, blank=True, verbose_name="Imię")
    surname = models.CharField(max_length=64, blank=True, verbose_name="Nazwisko")


class TruckTrailer(models.Model):
    truckSet = models.ForeignKey(Truck, on_delete=models.CASCADE)
    trailerSet = models.ForeignKey(Trailer, on_delete=models.CASCADE)


class TruckSetToWorker(models.Model):
    driver = models.ForeignKey(WorkerDriver, on_delete=models.CASCADE)
    truckSet = models.ForeignKey(TruckTrailer, on_delete=models.CASCADE)
