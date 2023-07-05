from rest_framework import serializers
from .models import *

class QoshiqchiSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ism = serializers.CharField(max_length=50)
    tugulgan_yil = serializers.DateField()
    davlat = serializers.CharField(max_length=50)


class AlbomSerializer(serializers.ModelSerializer):
    # albomlar = QoshiqchiSerializer(many=True)
    class Meta:
        model = Albom
        fields = '__all__'

class QoshiqSerializer(serializers.ModelSerializer):
    # albomlar = AlbomSerializer(many=True)
    class Meta:
        model = Qoshiq
        fields = '__all__'
    def validate_nom(self,  qiymat):
        for i in qiymat:
            if 'mp3' in i:
                raise serializers.ValidationError("bunday faylni yuklaash mumkun emas")
            return qiymat

    def validate_davomiylik(self, qiymat):
        if qiymat > '00:07:00':
            raise serializers.ValidationError("Xatolik!")
        return qiymat


class QoshiqchiSaqlashSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ism = serializers.CharField(max_length=50)
    tugulgan_yil = serializers.DateField()
    davlat = serializers.CharField(max_length=50)