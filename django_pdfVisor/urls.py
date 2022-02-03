from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from visor import views

router = routers.DefaultRouter()
router.register(r'visor', views.home, 'visor')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('visor/', include('visor.urls')),
]
