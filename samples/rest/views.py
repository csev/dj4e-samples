from rest.models import Breed, Cat
from rest_framework import viewsets
from rest.serializers import BreedSerializer, CatSerializer


class BreedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class CatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
