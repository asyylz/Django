from django.contrib import admin
from .models import Project

# Register your models here.

# We say hey, I want to see this model inside of th admin.
admin.site.register(Project)

