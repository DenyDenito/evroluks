from django.contrib import admin
from .models import Service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {'fields': ('title', 'description', 'short_description', 'image')}),
    )


admin.site.register(Service, ServiceAdmin)
