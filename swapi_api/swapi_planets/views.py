from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Planet
from .serializers import PlanetSerializer

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    #permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()