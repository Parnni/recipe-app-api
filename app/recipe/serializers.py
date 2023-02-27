from core.models import Ingredient, Recipe, Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]
        read_only_fields = ["id"]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name"]
        read_only_fields = ["id"]


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ["id", "title", "time", "price", "tags", "ingredients"]
        read_only_fields = ["id"]

    def _get_or_create_tags(self, instance, tags):
        auth_user = self.context["request"].user

        for tag in tags:
            tag_obj, _ = Tag.objects.get_or_create(**tag, user=auth_user)
            instance.tags.add(tag_obj)
        return instance

    def _get_or_create_ingredients(self, instance, ingredients):
        auth_user = self.context["request"].user

        for ingredient in ingredients:
            ingredient_obj, _ = Ingredient.objects.get_or_create(**ingredient, user=auth_user)
            instance.ingredients.add(ingredient_obj)
        return instance

    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        ingredients = validated_data.pop("ingredients", [])

        recipe = Recipe.objects.create(**validated_data)
        recipe = self._get_or_create_tags(recipe, tags)
        recipe = self._get_or_create_ingredients(recipe, ingredients)

        return recipe

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", None)
        ingredients = validated_data.pop("ingredients", None)

        if tags is not None:
            instance.tags.clear()
            instance = self._get_or_create_tags(instance, tags)

        if ingredients is not None:
            instance.ingredients.clear()
            instance = self._get_or_create_ingredients(instance, ingredients)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class RecipeDetailSerializer(RecipeSerializer):
    """More detailed serializer."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ["description", "link"]
