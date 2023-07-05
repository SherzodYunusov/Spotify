from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from django.contrib.postgres.search import TrigramSimilarity
from rest_framework import filters

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

class AlbomModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nom']
    ordering_fields = ['sana']

    @action(detail=True, methods=['GET', 'POST'])
    def qoshiq(self, request, pk):
        if request.method == 'POST':
            albom = request.data
            qoshiq = self.get_object()
            serializer = AlbomSerializer(data=albom)
            if serializer.is_valid():
                q = Qoshiq.objects.create(
                    nom = serializer.validated_data.get('nom'),
                    janr = serializer.validated_data.get('janr'),
                    davomiylik = serializer.validated_data.get('davomiylik'),
                    fayl = serializer.validated_data.get('fayl'),
                    albom = serializer.validated_data.get('albom'),
                )
                albom.qoshiq.add()
                albom.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        albom = self.get_object()
        qoshiq = albom.qoshiqchi.all()
        serializer = AlbomSerializer(qoshiq, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QoshiqModelViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nom', 'janr']
    ordering_fields = ['davomiylik']

class QoshiqchiModelViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ism', 'davlat']
    ordering_fields = ['tugulgan_yil']

# Create your views here.
