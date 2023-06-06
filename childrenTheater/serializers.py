from rest_framework import serializers
from .models import ChildreTheater

class ChildreTheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildreTheater
        fields=["title","image","director","actors","producer","production_date","release_date","create_date","publish_date"]
