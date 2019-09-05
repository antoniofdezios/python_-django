from Foods.models import Food
from rest_framework import viewsets
from .serializers import FoodSerializer



class FoodAPIViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

