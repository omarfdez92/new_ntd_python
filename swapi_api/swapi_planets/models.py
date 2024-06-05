from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=255,unique=True)
    population = models.CharField(max_length=255, null=True, blank=True)
    terrains = models.JSONField(default=list)
    climates = models.JSONField(default=list)

    def __str__(self):
        return self.name
