from django.urls import path
from . import views

urlpatterns = [
    path('<str:file>/<int:fromPage>/<int:toPage>', views.visor, name="visor"),
    path('translate/<str:sentence>', views.translator, name="tranlate")
]