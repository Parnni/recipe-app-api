from core.models import Recipe, Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]
        read_only_fields = ["id"]


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ["id", "title", "time", "price", "tags"]
        read_only_fields = ["id"]

    def _get_or_create(self, instance, tags):
        auth_user = self.context["request"].user

        for tag in tags:
            tag_obj, _ = Tag.objects.get_or_create(**tag, user=auth_user)
            instance.tags.add(tag_obj)
        return instance

    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        recipe = Recipe.objects.create(**validated_data)
        recipe = self._get_or_create(recipe, tags)
        return recipe

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", None)

        if tags is not None:
            instance.tags.clear()
            instance = self._get_or_create(instance, tags)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class RecipeDetailSerializer(RecipeSerializer):
    """More detailed serializer."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ["description", "link"]
