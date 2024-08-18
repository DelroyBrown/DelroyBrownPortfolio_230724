# DelroyBrownPortfolio_projects\models.py
from django.db import models


class ProjectDetails(models.Model):
    project_name = models.CharField(max_length=25, blank=False, null=False, default="")
    project_description = models.TextField(blank=False, null=False, default="")
    image_main = models.ImageField(upload_to="project-images", blank=False, null=False)
    image_1 = models.ImageField(upload_to="project-images", blank=False, null=False)
    image_2 = models.ImageField(upload_to="project-images", blank=True, null=True)
    image_3 = models.ImageField(upload_to="project-images", blank=True, null=True)

    def __str__(self):
        return self.project_name
