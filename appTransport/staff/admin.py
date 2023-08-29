from django.contrib import admin
from .models import *

@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    pass

@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    pass

@admin.register(WorkerDriver)
class WorkerDriverAdmin(admin.ModelAdmin):
    pass

@admin.register(TruckTrailer)
class TruckTrailerAdmin(admin.ModelAdmin):
    pass

@admin.register(TruckSetToWorker)
class TruckSetToWorkerAdmin(admin.ModelAdmin):
    pass
