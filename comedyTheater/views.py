from rest_framework import generics
from .models import ComedyTheater
from .serializers import ComedyTheaterSerializer

class ComedyTheaterListView(generics.ListCreateAPIView):
    queryset = ComedyTheater.objects.all()
    serializer_class = ComedyTheaterSerializer

class ComedyTheaterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComedyTheater.objects.all()
    serializer_class = ComedyTheaterSerializer

