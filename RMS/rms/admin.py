__author__ = 'gaojian'
from django.contrib import admin
from RMS.rms.models import Product, Backlog

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')

class BacklogAdmin(admin.ModelAdmin):
    list_display = ('stories', 'prioritized', 'estimated', 'value')


admin.site.register(Product, ProductAdmin)
admin.site.register(Backlog, BacklogAdmin)
