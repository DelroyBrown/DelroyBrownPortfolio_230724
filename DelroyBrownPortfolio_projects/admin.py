# DelroyBrownPortfolio_projects/admin.py
from django.contrib import admin
from .models import ProjectDetails, ProgLanguageUsed


@admin.register(ProjectDetails)
class ProjectDetailsAdmin(admin.ModelAdmin):
    filter_horizontal = (
        "prog_languages_used",
    )  # This makes the ManyToManyField easier to manage in the admin


admin.site.register(ProgLanguageUsed)
