from rest_framework import serializers

from .models import Planet, Recruit, Sith


class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planet
        fields = ('id', 'name')


class SithSerializer(serializers.HyperlinkedModelSerializer):
    planet = serializers.SerializerMethodField()
    class Meta:
        model = Sith
        fields = ('id', 'name', 'planet')
    def get_planet(self, obj):
        return obj.planet.name


class RecruitSerializer(serializers.HyperlinkedModelSerializer):
    planet = serializers.SerializerMethodField()
    class Meta:
        model = Recruit
        fields = (
            'id', 'name', 'planet',
            'age', 'email'
        )
    def get_planet(self, obj):
        return obj.planet.name







