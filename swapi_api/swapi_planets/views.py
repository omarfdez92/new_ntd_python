from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Planet
from .serializers import PlanetSerializer
from rest_framework.response import Response
from rest_framework import status

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    permission_classes = [permissions.IsAuthenticated]


    def destroy(self, request, *args, **kwargs):
          instance = self.get_object()
          self.perform_destroy(instance)
          return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
          try:
                return super().update(request, *args, **kwargs)
          except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


def index(request):
        planets = Planet.objects.all() #get planet data 
        return render(request, 'index.html', {'planets': planets}) #pass it to template