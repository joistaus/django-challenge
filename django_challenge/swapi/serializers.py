from rest_framework import serializers
from .models import Planet, Terrain, Climate

class PlanetSerializer(serializers.ModelSerializer):
    terrains = serializers.ListField(
        child=serializers.CharField(), write_only=True
    )
    climates = serializers.ListField(
        child=serializers.CharField(), write_only=True
    )

    terrains_list = serializers.SerializerMethodField(read_only=True)
    climates_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Planet
        fields = ['id', 'name', 'population', 'terrains', 'climates', 'terrains_list', 'climates_list']

    def get_terrains_list(self, obj):
        return [terrain.name for terrain in obj.terrains.all()]

    def get_climates_list(self, obj):
        return [climate.name for climate in obj.climates.all()]

    def create(self, validated_data):
        terrain_names = validated_data.pop('terrains', [])
        climate_names = validated_data.pop('climates', [])

        planet = Planet.objects.create(**validated_data)
        planet.terrains.set(self._get_or_create_terrains(terrain_names))
        planet.climates.set(self._get_or_create_climates(climate_names))
        return planet

    def update(self, instance, validated_data):
        terrain_names = validated_data.pop('terrains', None)
        climate_names = validated_data.pop('climates', None)

        instance.name = validated_data.get('name', instance.name)
        instance.population = validated_data.get('population', instance.population)
        instance.save()

        if terrain_names is not None:
            instance.terrains.set(self._get_or_create_terrains(terrain_names))
        if climate_names is not None:
            instance.climates.set(self._get_or_create_climates(climate_names))

        return instance

    def _get_or_create_terrains(self, names):
        return [Terrain.objects.get_or_create(name=name)[0] for name in names]

    def _get_or_create_climates(self, names):
        return [Climate.objects.get_or_create(name=name)[0] for name in names]
