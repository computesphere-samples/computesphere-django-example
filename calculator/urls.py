from django.urls import path
from .views import calculate_age

urlpatterns = [
    path('', calculate_age, name='calculate_age'),
]
