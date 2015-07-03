from django.contrib import admin
from .models import Order
from .models import Slide


class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model = Order

    list_display = ['name', 'phone', 'email', 'date_execution', 'address', 'message', 'date']
    readonly_fields = ['name', 'phone', 'email', 'date_execution', 'address', 'message', 'date']
    search_fields = ['name', 'phone']
    list_filter = ['date', 'date_execution']

    def __str__(self):
        return u'%s' % self.name


class SlidesAdmin(admin.ModelAdmin):
    class Meta:
        model = Slide


admin.site.register(Slide, SlidesAdmin)
admin.site.register(Order, OrderAdmin)
