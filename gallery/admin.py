from django.contrib import admin

# Register your models here.
from .models import Album, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 5


class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "caption"]
    fieldsets = [
        (None, {'fields': ['title', 'caption']}),
    ]
    inlines = [ImageInline]


admin.site.register(Album, AlbumAdmin)
