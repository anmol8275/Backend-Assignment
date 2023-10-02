from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from django.utils.translation import gettext_lazy as _

from api.models import Post

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = [
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "is_superuser",
        "is_active",
    ]
    search_fields = ["first_name", "last_name", "email"]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "is_active",
                    "is_superuser",
                    "groups",
                ),
            },
        ),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "title", "created_at"]
    readonly_fields = ("created_at",)
    search_fields = ["user", "title"]
