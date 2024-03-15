from typing import Any
from django.views.generic import ListView, DetailView, TemplateView
from .models import Service, Order, Executor, Customer

class MainPageView(TemplateView):
    template_name = 'basic/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Main page'
        return context