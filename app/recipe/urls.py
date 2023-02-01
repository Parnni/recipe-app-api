"""Generate URLs using Router as ModelViewSet is used."""

from django.urls import include, path
from recipe import views
from rest_framework.routers import DefaultRouter

app_name = "recipe"

router = DefaultRouter()
router.register("recipes", views.RecipeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
