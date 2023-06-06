from django.urls import path
from .views import ArtAndExpriensListView,ArtAndExpriensDetailView

urlpatterns=[
    path("", ArtAndExpriensListView.as_view(),name="artandexprienslist"),
    path("<int:pk>", ArtAndExpriensDetailView.as_view(),name="cartandexpriensedetail"),
]