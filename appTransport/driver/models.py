from django.contrib.auth.models import (
    AbstractBaseUser,
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
    User
)
from django.db import models
from django.db.models import Q
from forwarding.models import Info_transport
from staff.models import Trailer, Truck

DRIVE_LICENSE = [
    ("C", "C"),
    ("C+E", "C+E"),
]


STATUS_CHOICES = [
    ("on_site", "Na miejscu"),
]


STATUS_SERVICES = [("Yes", "Przesmarowany"), ("No", "Nie przesmarowany")]

STATUS_FUEL = [("Yes", "Zatankowany"), ("No", "Nie zatankowany")]


LOADING_STATUS_CHOICES = [
    ("loaded", "Załadowany"),
    ("waiting_for_loading", "Oczekiwanie na załadunek"),
]


UNLOADING_STATUS_CHOICES = [
    ("unloaded", "Rozładowany"),
    ("waiting_for_unloading", "Oczekiwanie na rozładunek"),
]

USER = (
    ('admin', 'Admin'),
    ('manager', 'Manager'),
    ('personnel', 'Personnel'),
    ('dispatcher', 'Dispatcher'),
    ('forwarder', 'Forwarder'),
    ('driver', 'Driver'),
)


# class CustomUser(AbstractUser):
#     first_name = models.CharField(max_length=30, blank=True, verbose_name="Imię")
#     last_name = models.CharField(max_length=30, blank=True, verbose_name="Nazwisko")
#     phone_number = models.CharField(
#         max_length=10, unique=True, blank=True, verbose_name="Numer telefonu"
#     )
#     drive_license = models.CharField(
#         choices=DRIVE_LICENSE, blank=True, verbose_name="Prawo jazdy"
#     )
#     email_address = models.EmailField(unique=True, blank=True, verbose_name="Email")

#     # def __str__(self):
#     #     return self.firs_name + self.last_name


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, phone_number, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, phone_number=phone_number, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, phone_number, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")

#         return self.create_user(email, phone_number, password, **extra_fields)

#     def get_by_natural_key(self, value):
#         return self.get(
#             Q(email__iexact=value)
#             | Q(phone_number__iexact=value)
#         )

#     def authenticate(self, request, phone_number=None, password=None, **kwargs):
#         user = self.get_by_natural_key(phone_number)
#         if user.check_password(password) and self.user_can_authenticate(user):
#             return user


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = None
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(
#         max_length=10, unique=True, blank=True, verbose_name="Numer telefonu"
#     )
#     drive_license = models.CharField(
#         choices=DRIVE_LICENSE, blank=True, verbose_name="Prawo jazdy"
#     )
#     first_name = models.CharField(max_length=30, blank=True, verbose_name="Imię")
#     last_name = models.CharField(max_length=30, blank=True, verbose_name="Nazwisko")
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
    
#     date_joined = models.DateTimeField(auto_now_add=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = "phone_number"
#     REQUIRED_FIELDS = ["email"]

#     def __str__(self):
#         return f"{self.first_name[0].upper()} {self.last_name.capitalize()}"

#     def get_by_natural_key(self, value):
#         return self.__class__.objects.get(
#             Q(email__iexact=value)
#             | Q(phone_number__iexact=value)
#         )

class CustomUserManager(BaseUserManager):
    def _create_user(self, phone_number, email, user_type, first_name, last_name, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The given phone number must be set')
        if not email:
            raise ValueError('The given email must be set')
        if not user_type:
            raise ValueError('The given user type must be set')
        if not first_name:
            raise ValueError('The given first name must be set')
        if not last_name:
            raise ValueError('The given last name must be set')
        user = self.model(phone_number=phone_number, email=email, user_type=user_type, first_name=first_name, last_name=last_name,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, email, user_type, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, email, user_type, first_name, last_name, password, **extra_fields)

    def create_superuser(self, phone_number, email, user_type, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, email, user_type, first_name, last_name, password, **extra_fields)


class CustomUser(AbstractUser):

    username = None
    phone_number = models.CharField(max_length=15, blank=False, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    user_type = models.CharField(max_length=20, choices=USER)
    driving_license = models.CharField(max_length=5, choices=DRIVE_LICENSE, verbose_name="driving_license")
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'user_type', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.full_name().title()} : {self.phone_number} ({self.user_type.title()})'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True



class Info_of_truck(models.Model):
    driver_name = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, verbose_name="Kierowca"
    )
    truck_number = models.ForeignKey(
        Truck,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Rejestracja ciężarówki",
    )
    trailer_number = models.ForeignKey(
        Trailer,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Rejestracja przyczepy",
    )
    mileage = models.DecimalField(
        max_digits=8, decimal_places=1, verbose_name="Przebieg", blank=True
    )
    fuel = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="Tankowanie", blank=True
    )
    service = models.CharField(choices=STATUS_SERVICES, verbose_name="Serwis")
    description = models.TextField(verbose_name="Uwagi")


class Status_of_load(models.Model):
    loading_status = models.CharField(choices=LOADING_STATUS_CHOICES)
    unloading_status = models.CharField(choices=UNLOADING_STATUS_CHOICES)


class Load_info(models.Model):
    load_info = models.OneToOneField(Info_transport, on_delete=models.CASCADE)
