from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL = reverse("user:create")


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class TestPublicUserAPI(TestCase):
    """Test for non-authenticated users."""

    def setUp(self) -> None:
        self.client = APIClient()

    def test_user_create_success(self):
        payload = {
            "email": "publicuser@gmail.com",
            "password": "publicuser",
            "name": "PublicUser",
        }
        resp = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertNotIn("password", resp.data)

        created_user = get_user_model().objects.get(email=payload["email"])
        self.assertEqual(payload["email"], created_user.email)
        self.assertTrue(create_user.check_password(payload["password"]))

    def test_user_exits_error(self):
        payload = {
            "email": "publicuser@gmail.com",
            "password": "publicuser",
            "name": "PublicUser",
        }
        create_user(**payload)
        resp = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        payload = {
            "email": "publicuser@gmail.com",
            "password": "p",
            "name": "PublicUser",
        }

        resp = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
