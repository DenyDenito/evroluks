from django.contrib import admin
from .models import Promo

# Register your models here.

class PromoAdmin(admin.ModelAdmin):
    list_display = ('date', 'title')
    list_display_links = ('title',)
    list_filter = ('date',)
    # date_hierarchy = 'date'
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {'fields': ('title', 'description', 'short_description', 'image')}),
        ('Настройки', {'fields': ('date',)}),
    )


admin.site.register(Promo, PromoAdmin)
