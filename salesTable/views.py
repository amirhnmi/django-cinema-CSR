from rest_framework import generics
from .models import SalesTable
from .serializers import SalesTableSerializer


class SalesTableListView(generics.ListCreateAPIView):
    queryset = SalesTable.objects.all()
    serializer_class = SalesTableSerializer


class SalesTableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesTable.objects.all()
    serializer_class = SalesTableSerializer
