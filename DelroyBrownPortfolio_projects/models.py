# DelroyBrownPortfolio_projects\models.py
from django.db import models


class ProgLanguageUsed(models.Model):
    language_name = models.CharField(max_length=50, blank=False, null=False, default="")

    def __str__(self):
        return self.language_name


class ProjectDetails(models.Model):
    project_name = models.CharField(max_length=25, blank=False, null=False, default="")
    project_description = models.TextField(blank=False, null=False, default="")
    image_main = models.ImageField(upload_to="project-images", blank=False, null=False)
    image_1 = models.ImageField(upload_to="project-images", blank=False, null=False)
    image_2 = models.ImageField(upload_to="project-images", blank=True, null=True)
    image_3 = models.ImageField(upload_to="project-images", blank=True, null=True)
    prog_languages_used = models.ManyToManyField(ProgLanguageUsed)
    prog_language_reason = models.TextField(blank=False, null=False, default="")

    def __str__(self):
        return self.project_name
