from rest_framework import serializers
from .models import Screening

class ScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screening
        fields=["title","image","director","actors","producer","production_date","release_date","create_date","publish_date"]
