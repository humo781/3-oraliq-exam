from django.contrib import admin
from .models import Catalog

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('name', 'created_at')
    ordering = ('created_at',)
