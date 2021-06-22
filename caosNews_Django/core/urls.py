from django.urls import path
from .views import index

urlpattterns = [
    path('', index, name="index"),
]