from rest_framework import serializers
from .models import ComedyTheater

class ComedyTheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComedyTheater
        fields=["title","image","director","actors","producer","production_date","release_date","create_date","publish_date"]
