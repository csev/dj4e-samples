from rest.models import Breed, Cat
from rest_framework import serializers

class BreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = ( 'name', )

class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        # fields = '__all__'
        fields = ( 'nickname', 'weight', 'foods', 'breed' )

