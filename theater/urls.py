from django.urls import path
from .views import TheaterListView,TheaterDetailView

urlpatterns=[
    path("", TheaterListView.as_view(),name="theaterlist"),
    path("<int:pk>", TheaterDetailView.as_view(),name="theaterdetail"),
]