from rest_framework import serializers
from .models import *

class QoshiqchiSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ism = serializers.CharField(max_length=50)
    tugulgan_yil = serializers.DateField()
    davlat = serializers.CharField(max_length=50)


class AlbomSerializer(serializers.ModelSerializer):
    qoshiqchilar = QoshiqchiSerializer(many=True)
    class Meta:
        model = Albom
        field = '__all__'

class QoshiqSerializer(serializers.ModelSerializer):
    albomlar = AlbomSerializer(many=True)
    class Meta:
        model = Qoshiq
        field = '__all__'

class QoshiqchiSaqlashSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ism = serializers.CharField(max_length=50)
    tugulgan_yil = serializers.DateField()
    davlat = serializers.CharField(max_length=50)