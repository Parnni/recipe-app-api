from core.models import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["id", "title", "time", "price"]
        read_only_fields = ["id"]


class RecipeDetailSerializer(RecipeSerializer):
    """More detailed serializer."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ["description", "link"]
