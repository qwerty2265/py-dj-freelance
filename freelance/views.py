from django.views.generic import (
    ListView, 
    DetailView, 
    TemplateView,
    CreateView,
    UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

from .models import Service, Order, Executor, Customer

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")

class MainPageView(TemplateView):
    template_name = "basic/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Это главная страница проекта"
        return context