from django.views.generic import ListView, CreateView, UpdateView
from .models import Service
from .forms import ServiceForm

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    extra_context = {'title': 'Список услуг'}

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_form.html'
    extra_context = {'title': 'Создание услуги'}
    success_url = '/services/'

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_form.html'
    extra_context = {'title': 'Редактирование услуги'}
    success_url = '/services/'
