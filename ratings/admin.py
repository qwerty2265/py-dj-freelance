from django.contrib import admin
from .models import RatingOrder

@admin.register(RatingOrder)
class RatingOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'order_rating', 'testimonial')
    search_fields = ('order__title', 'user__user__username', 'testimonial')
