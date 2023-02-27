from core.models import Recipe, Tag
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from recipe.serializers import RecipeSerializer
from rest_framework import status
from rest_framework.test import APIClient

RECIPE_URL = reverse("recipe:recipe-list")
TAG_URL = reverse("recipe:tag-list")


def create_recipe(user):
    payload = {
        "user": user,
        "title": "Al faham",
        "description": "",
        "time": 30,
        "price": 300,
        "link": "somelink.com",
    }

    return Recipe.objects.create(**payload)


class TestPublicRecipeAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(**{"email": "test@email.com", "password": "testpassword"})

    def test_unauthenticated_user(self):
        recipe = create_recipe(self.user)
        resp = self.client.get(RECIPE_URL)

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


class TestPrivateRecipeAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(**{"email": "test@email.com", "password": "testpassword"})
        self.client.force_authenticate(self.user)

    def test_authenticated_user(self):
        create_recipe(self.user)
        create_recipe(self.user)

        resp = self.client.get(RECIPE_URL)

        recipe = Recipe.objects.all().order_by("-id")
        serializer = RecipeSerializer(recipe, many=True)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, serializer.data)


class TestCreateRecipeAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(**{"email": "test@email.com", "password": "testpassword"})
        self.client.force_authenticate(self.user)

    def test_create_recipe(self):
        payload = {
            "title": "Al faham",
            "time": 30,
            "price": 300,
        }

        resp = self.client.post(RECIPE_URL, payload)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        recipe = Recipe.objects.get(id=resp.data["id"])

        for field, value in payload.items():
            self.assertEqual(getattr(recipe, field), value)
        self.assertEqual(recipe.user, self.user)


class TestPublicTag(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(**{"email": "test@email.com", "password": "testpassword"})

    def test_create_tag(self):
        payload = {"user": self.user, "name": "Testtag"}
        resp = self.client.post(TAG_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


class TestPublicTag(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(**{"email": "test@email.com", "password": "testpassword"})
        self.client.force_authenticate(user=self.user)

    def test_create_tag(self):
        payload = {"user": self.user, "name": "Testtag"}
        resp = self.client.post(TAG_URL, payload)

        tag = Tag.objects.get(id=resp.data["id"])

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(tag.user, payload["user"])
        self.assertEqual(tag.name, payload["name"])
