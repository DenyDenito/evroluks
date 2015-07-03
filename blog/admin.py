from django.contrib import admin
from .models import BlogEntry

# Register your models here.

class BlogEntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    list_display = ('date', 'title')
    list_display_links = ('title',)
    list_filter = ('date',)
    # date_hierarchy = 'date'
    search_fields = ('title', 'body')
    fieldsets = (
        (None, {'fields': ('title', 'body', 'picture')}),
        ('Настройки', {'fields': ('date', 'slug')}),
    )


admin.site.register(BlogEntry, BlogEntryAdmin)
