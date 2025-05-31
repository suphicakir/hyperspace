from django.contrib import admin
from .models import Services

@admin.register(Services)
class ServicesAdmin (admin.ModelAdmin):
    list_display=('_title','_isFutured','_slug',)
    search_fields=('_title','_description')
    list_filter=('_isFutured',)
