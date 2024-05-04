from django.contrib import admin
from .models import Project, TodoItem

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Project)