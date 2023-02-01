"""
Django admin customization.
"""
from core import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as translator


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "name"]
    add_fieldsets = ((None, {"fields": ["email", "password1", "password2", "is_active", "is_superuser", "is_staff"]}),)
    fieldsets = (
        (translator("User"), {"fields": ["name", "email"]}),
        (translator("Permissions"), {"fields": ["is_active", "is_staff", "is_superuser"]}),
        (translator("Important dates"), {"classes": ("collapse",), "fields": ["last_login"]}),
    )
    readonly_fields = ["last_login"]


class RecipeAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "time", "price"]
    ordering = ["time", "price"]
    search_fields = ["user", "title"]


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
