from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'executor', 'description', 'service_type')
# Register your models here.

class OrderRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order__title', 'status')

admin.site.register(Service, ServiceAdmin)
