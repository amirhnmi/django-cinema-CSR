from rest_framework import generics
from .models import ArtAndExpriens
from .serializers import ArtAndExpriensSerializer

class ArtAndExpriensListView(generics.ListCreateAPIView):
    queryset = ArtAndExpriens.objects.all()
    serializer_class = ArtAndExpriensSerializer

class ArtAndExpriensDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtAndExpriens.objects.all()
    serializer_class = ArtAndExpriensSerializer

