from django.urls import path
from user import views

# Creating reverse proxy "user:create"
app_name = "user"

urlpatterns = [
    path("create/", views.CreateUserAPI.as_view(), name="create"),
]
