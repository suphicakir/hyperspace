from django.contrib import admin
from .models import Services

@admin.register(Services)
class ServicesAdmin (admin.ModelAdmin):
    list_display=('Title','IsFeatured','Slug',)
    search_fields=('Title','Description')
    list_filter=('IsFeatured',)
