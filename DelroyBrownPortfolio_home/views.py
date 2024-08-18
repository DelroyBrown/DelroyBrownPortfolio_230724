from django.shortcuts import render
from DelroyBrownPortfolio_projects.models import ProjectDetails


def home(request):
    projects = ProjectDetails.objects.all()
    return render(request, "home/home.html", {"projects": projects})
