from django.contrib import admin

from .models import Property, Category, Reserver


# Register your models here.
class PropertAdmin(admin.ModelAdmin):
    list_display = ['name', 'property_type', 'category', 'area', 'bed_number', 'bath_number', 'garages_number', 'image',
                    'location']
    search_fields = ['name', 'property_type']
    list_filter = ['category', 'property_type']


admin.site.register(Property, PropertAdmin)
admin.site.register(Category)
admin.site.register(Reserver)
