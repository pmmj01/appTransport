"""
URL configuration for appTransport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from driver.views import UserRegistration
from staff.views import DataAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('driver/', include('driver.urls')),
    path("staff/", include("staff.urls")),
    path("api/data/", DataAPIView.as_view(), name="data-api"),
    path("register-driver/", UserRegistration.as_view(), name="register-driver"),
]
