from django.urls import path
from . import views
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name="ia"),
    path('', Index.as_view(), name="enregistrer_recherche"),
]