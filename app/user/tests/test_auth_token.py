from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

CREATE_TOKEN_URL = reverse("user:token")


def create_user(payload):
    return get_user_model().objects.create_user(**payload)


class TestAuthentication(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_token(self):
        payload = {
            "email": "test@example.com",
            "password": "testpassword",
            "name": "Test",
        }

        create_user(payload)

        payload = {
            "email": payload["email"],
            "password": payload["password"],
        }

        resp = self.client.post(CREATE_TOKEN_URL, data=payload)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn("token", resp.data)
