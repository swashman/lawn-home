"""App URLs"""

# Django
from django.urls import path

# Lawn Home
from lawnhome import views

app_name: str = "lawnhome"

urlpatterns = [
    path("", views.index, name="index"),
]
