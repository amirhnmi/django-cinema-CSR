from rest_framework import serializers
from screenings import models as screeninimodel
from theater import models as theatermodel
from artAndExpriens import models as artandexpriensmodel
from comedyTheater import models as comedytheatermodel
from childrenTheater import models as childrentheatermodel
from salesTable import models as salestablemodel
from news import models as newsmodel


class ScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = screeninimodel.Screening
        fields=["title","image","director","actors","producer","production_date","release_date","create_date","publish_date"]
        

class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = theatermodel.Theater
        fields=["title","image","director","actors","producer","production_date","release_date","create_date","publish_date"]
        

class ArtAndExprienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = artandexpriensmodel.ArtAndExpriens
        fields=["title","image","director","actors","producer","production_date","release_date","create_date","publish_date"]


class ComedyTheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = comedytheatermodel.ComedyTheater
        fields=["title","image","director","actors","producer","production_date","release_date","create_date","publish_date"]

class ChildrenTheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = childrentheatermodel.ChildreTheater
        fields=["title","image","director","actors","producer","production_date","release_date","create_date","publish_date"]


class SalesTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = salestablemodel.SalesTable
        fields=["title","image","director","actors","producer","production_date","release_date","create_date","publish_date"]


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = newsmodel.News
        fields=["title","image","director","actors","producer","production_date","release_date","create_date","publish_date"]
