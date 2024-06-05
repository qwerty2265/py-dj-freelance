from django.urls import path
from .views import RatingListView, RatingUpdateView

urlpatterns = [
    path("all", RatingListView.as_view(), name="rating_list"),
    path("update/<int:order>/", RatingUpdateView.as_view(), name="rating_update"),
]
