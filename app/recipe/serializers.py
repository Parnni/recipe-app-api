from core.models import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["id", "user", "title", "description", "time", "price", "link"]
        read_only_fields = ["id"]
