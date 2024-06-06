from django.contrib import admin
from .models import RatingOrder, Testimonial

@admin.register(RatingOrder)
class RatingOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'order_rating', 'testimonial')
    search_fields = ('order__title', 'user__user__username', 'testimonial')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'testimonial')
    search_fields = ('user__username', 'order__id')
