"""API for creating a user."""

from rest_framework.generics import CreateAPIView
from user.serializers import UserSerializer


class CreateUserAPI(CreateAPIView):
    serializer_class = UserSerializer
