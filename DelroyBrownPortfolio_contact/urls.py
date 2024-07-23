from django.urls import path
from . import views

app_name = "DelroyBrownPortfolio_contact"

urlpatterns = [
    path("contact-me", views.contact, name="contact"),
]
