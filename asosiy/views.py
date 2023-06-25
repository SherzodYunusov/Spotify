from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializer import *

class QoshiqchiApiView(APIView):
    def get(self, request):
        qoshiqchi = Qoshiqchi.objects.all()
        serializers = QoshiqchiSerializer(qoshiqchi, many=True)
        return Response(serializers.data)

    def post(self, request):
        qoshiqchi = request.data
        serializers = QoshiqchiSerializer(data=qoshiqchi)
        if serializers.is_valid():
            Qoshiqchi.objects.create(
                ism = serializers.validated_data.get('ism'),
                tugulgan_yil = serializers.validated_data.get('tugulgan_yil'),
                davlat = serializers.validated_data.get('davlat'),
            )
            return Response(serializers.data)
        return Response(serializers.errors)

class QoshiqchiChangeApiView(APIView):
    def put(self, request, pk):
        # qoshiqchi = Qoshiqchi.objects.get(id=pk)
        malumot = request.data
        serializers = QoshiqchiSaqlashSerializer(data=malumot)
        if serializers.is_valid():
            Qoshiqchi.objects.filter(id=pk).update(
                ism=serializers.validated_data.get('ism'),
                tugulgan_yil=serializers.validated_data.get('tugulgan_yil'),
                davlat=serializers.validated_data.get('davlat'),
            )
            return Response(serializers.data)
        return Response(serializers.errors)
# Create your views here.
