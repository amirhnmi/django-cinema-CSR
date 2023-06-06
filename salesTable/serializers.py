from rest_framework import serializers
from .models import SalesTable

class SalesTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesTable
        fields=["movie_name","image","director","price","last_update"]
