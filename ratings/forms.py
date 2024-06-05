from django import forms
from django.forms import ModelForm
from .models import RatingOrder

class RatingForm(ModelForm):
    class Meta:
        model = RatingOrder
        fields = ["order", "testimonial", "user", "order_rating"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["order"].widget = forms.HiddenInput()
        self.fields["user"].widget = forms.HiddenInput()
