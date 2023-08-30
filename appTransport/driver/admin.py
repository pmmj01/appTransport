from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, Info_of_truck, Load_info, Status_of_load

# @admin.register(CustomUser)
# class UserAdmin(UserAdmin):
#     list_display = (
#         "first_name",
#         "last_name",
#         "phone_number",
#         "drive_license",
#         "email_address",
#     )


# admin.site.register(CustomUser, UserAdmin)


class CustomUserAdmin(BaseUserAdmin):
    #     ordering = ["email"]  # Ustaw pole unikalne, które chcesz używać do sortowania
    #     list_display = [
    #         "email",
    #         "phone_number",
    #         "first_name",
    #         "last_name",
    #         "is_active",
    #     ]  # Dodaj pola, które chcesz wyświetlać w liście użytkowników
    #     search_fields = [
    #         "phone_number",
    #         "email",
    #     ]  # Pola, po których możesz wyszukiwać użytkowników
    #     fieldsets = (
    #         (None, {"fields": ("email", "password")}),
    #         (
    #             "Personal Info",
    #             {"fields": ("first_name", "last_name", "phone_number", "drive_license")},
    #         ),
    #         (
    #             "Permissions",
    #             {
    #                 "fields": (
    #                     "is_active",
    #                     "is_staff",
    #                     "is_superuser",
    #                     "groups",
    #                     "user_permissions",
    #                 )
    #             },
    #         ),
    #         ("Important dates", {"fields": ("last_login", "date_joined")}),
    #     )

    #     add_fieldsets = (
    #         (
    #             None,
    #             {
    #                 "classes": ("wide",),
    #                 "fields": ("email", "password1", "password2"),
    #             },
    #         ),
    #     )

    # admin.site.register(get_user_model(), CustomUserAdmin)

    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "email",
                    "last_name",
                    "driving_license",
                    "user_type",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "driving_license",
                    "user_type",
                    "is_staff",
                ),
            },
        ),
    )
    list_display = (
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "user_type",
        "driving_license",
        "is_staff",
    )
    search_fields = (
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "user_type",
        "driving_license",
    )
    ordering = ("phone_number",)


admin.site.register(get_user_model(), CustomUserAdmin)


@admin.register(Info_of_truck)
class InfoOfTruckAdmin(admin.ModelAdmin):
    pass


@admin.register(Status_of_load)
class StatusOfLoadAdmin(admin.ModelAdmin):
    pass


@admin.register(Load_info)
class LoadInfoAdmin(admin.ModelAdmin):
    pass
