from django.db import models

class FlattenedJsonModel(models.Model):
    inputJson = models.JSONField()
    flattenedJson = models.JSONField(null=True, blank=True)
