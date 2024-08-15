from django.shortcuts import render
from orders.models import Order
from services.models import Service
from django.contrib.auth.models import User

def index(request):
    orders = Order.objects.all()
    services = Service.objects.all()
    users = User.objects.all()
    return render(request, 'mainpage/index.html', {
        'orders': orders,
        'services': services,
        'users': users
    })
