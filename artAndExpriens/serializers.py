from rest_framework import serializers
from .models import ArtAndExpriens

class ArtAndExpriensSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtAndExpriens
        fields=["title","image","director","actors","producer","production_date","release_date","create_date","publish_date"]
