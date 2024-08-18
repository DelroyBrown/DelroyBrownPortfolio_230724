# DelroyBrownPortfolio_projects/urls.py
from django.urls import path
from . import views

app_name = "DelroyBrownPortfolio_projects"

urlpatterns = [
    path("projects/", views.projects_list, name="projects-list"),
    path("projects/<int:project_id>/", views.project_detail, name="project-detail"),
]
