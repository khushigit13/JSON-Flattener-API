from django.contrib import admin
from django.urls import path,include
from .views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",homePage),
    path("api/",include('api.urls')),
]
