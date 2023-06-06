from django.urls import path
from .views import ComedyTheaterListView,ComedyTheaterDetailView

urlpatterns=[
    path("", ComedyTheaterListView.as_view(),name="comedytheaterlist"),
    path("<int:pk>", ComedyTheaterDetailView.as_view(),name="comedytheaterlist"),
]