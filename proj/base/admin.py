from django.contrib import admin
from . import models

@admin.register(models.FileDemo)
class FileDemoAdmin(admin.ModelAdmin):
  list_display = ['id', 'file', 'img']
  
  class Meta:
    pass