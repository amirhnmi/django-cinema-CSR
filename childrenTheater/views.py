from rest_framework import generics
from .models import ChildreTheater
from .serializers import ChildreTheaterSerializer

class ChildreTheaterListView(generics.ListCreateAPIView):
    queryset = ChildreTheater.objects.all()
    serializer_class = ChildreTheaterSerializer

class ChildreTheaterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChildreTheater.objects.all()
    serializer_class = ChildreTheaterSerializer

