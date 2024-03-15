from django.urls import path
from .views import MainPageView

urlpatters = [
    path('', MainPageView.as_view(), name='main_page'),
]
