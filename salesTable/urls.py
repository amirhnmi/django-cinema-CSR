from django.urls import path
from .views import SalesTableListView,SalesTableDetailView

urlpatterns=[
    path("", SalesTableListView.as_view(),name="salestablelist"),
    path("<int:pk>", SalesTableDetailView.as_view(),name="salestabledetail"),
]