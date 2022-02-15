from django.urls import path
from . import views

urlpatterns = [
    path('<str:file>', views.visor, name="visor"),
    path('translate/<str:sentence>', views.translator, name="tranlate")
]