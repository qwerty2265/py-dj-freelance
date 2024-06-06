from django.db import models
from freelance.models import Order, UserProfile

class RatingOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    testimonial = models.TextField()
    order_rating = models.FloatField()

    class Meta:
        unique_together = ("order", "user")

    def __str__(self):
        return f"Rating for Order {self.order} by {self.user}"

class Testimonial(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь")
    testimonial = models.TextField(verbose_name="Отзыв")

    def __str__(self):
        return f"Отзыв от {self.user.username} по заказу {self.order.id}"