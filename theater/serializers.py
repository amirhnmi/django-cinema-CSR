from rest_framework import serializers
from .models import Theater

class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields=["title","image","director","actors","producer","production_date","release_date","create_date","publish_date"]
