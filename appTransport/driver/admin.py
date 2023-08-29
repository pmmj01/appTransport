from django.contrib import admin
from .models import Info_of_truck, Status_of_load, Load_info, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Info_of_truck)
class InfoOfTruckAdmin(admin.ModelAdmin):
    pass

@admin.register(Status_of_load)
class StatusOfLoadAdmin(admin.ModelAdmin):
    pass

@admin.register(Load_info)
class LoadInfoAdmin(admin.ModelAdmin):
    pass