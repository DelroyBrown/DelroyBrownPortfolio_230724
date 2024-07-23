from django.urls import path
from . import views

app_name = "DelroyBrownPortfolio_about"

urlpatterns = [
    path("about-me", views.about, name="about-me"),
]
