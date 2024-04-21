from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class CarViewSets(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    ilterset_fields = ['category','marka', 'model', 'price', 'year', 'price']
    search_fields = ['marka']


class BetViewSets(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]