# DelroyBrownPortfolio_projects\views.py
from django.shortcuts import render, get_object_or_404
from .models import ProjectDetails


def projects_list(request):
    projects = ProjectDetails.objects.all()
    return render(request, "projects/projects_list.html", {"projects": projects})


def project_detail(request, project_id):
    project = get_object_or_404(ProjectDetails, id=project_id)
    return render(request, "projects.project_detail.html", {"project": project})
