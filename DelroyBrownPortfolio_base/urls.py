from django.contrib import admin
from django.urls import path, include

app_name = 'DelroyBrownPortfolio_base'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("DelroyBrownPortfolio_home.urls")),
    path("", include("DelroyBrownPortfolio_about.urls")),
    path("", include("DelroyBrownPortfolio_contact.urls")),
]
