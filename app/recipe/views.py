from core.models import Ingredient, Recipe, Tag
from recipe import serializers
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """User specific."""
        return self.queryset.filter(user=self.request.user).order_by("-id")

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.RecipeSerializer
        elif self.action == "upload_image":
            return serializers.RecipeImageSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """The will be validated first."""
        serializer.save(user=self.request.user)

    @action(methods=["POST"], detail=True, url_path="upload-image")
    def upload_image(self, request, pk=None):
        recipe = self.get_object()
        serializer = self.get_serializer(recipe, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class BaseRecipeAttrView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by("name")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrView):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipeAttrView):
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
