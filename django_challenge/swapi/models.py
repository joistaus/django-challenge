from django.db import models

class Terrain(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Climate(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Planet(models.Model):
    name = models.CharField(max_length=100)
    population = models.FloatField()
    terrains = models.ManyToManyField(Terrain, related_name='planets')
    climates = models.ManyToManyField(Climate, related_name='planets')

    def __str__(self):
        return self.name
