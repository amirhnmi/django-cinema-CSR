from django.urls import path
from .views import ChildreTheaterListView,ChildreTheaterDetailView

urlpatterns=[
    path("", ChildreTheaterListView.as_view(),name="childrentheaterlist"),
    path("<int:pk>", ChildreTheaterDetailView.as_view(),name="childrentheaterlist"),
]