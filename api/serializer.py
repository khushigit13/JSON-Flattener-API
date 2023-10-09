from rest_framework import serializers
from .models import FlattenedJsonModel

class FlattenedJsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlattenedJsonModel
        fields = '__all__'
        