from django.contrib import admin
from .models import *


@admin.register(Consumer_data)
class ConsumerDataAdmin(admin.ModelAdmin):
    pass

@admin.register(Load_data)
class LoadDataAdmin(admin.ModelAdmin):
    pass

@admin.register(Info_transport)
class InfoTransportAdmin(admin.ModelAdmin):
    pass

# @admin.register(Load_data)
# class ConsumerDataAdmin(admin.ModelAdmin):
#     pass