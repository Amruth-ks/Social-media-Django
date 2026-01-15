from django.contrib import admin
from .models import Species

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ("name", "scientific_name", "cash_value")
    search_fields = ("name", "scientific_name")
    list_filter = ("cash_value",)
