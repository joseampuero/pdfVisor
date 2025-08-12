from django.urls import path
from . import views

urlpatterns = [
    path('<str:file>/<int:fromPage>/<int:toPage>', views.visor, name="visor"),
    path('translate/<str:sentence>', views.translator, name="translate"),  # GET - palabras simples
    path('translate/', views.translator_post, name="translate_post"),      # POST - frases largas
    path('<int:fromPage>/<int:toPage>', views.learn, name="learn")
]