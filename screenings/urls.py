from django.urls import path
from .views import ScreeningListView,ScreeningDetailView

urlpatterns=[
    path("", ScreeningListView.as_view(),name="screeninglist"),
    path("<int:pk>", ScreeningDetailView.as_view(),name="screeningdetail"),
]