# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom user model
    """
    email = models.EmailField(
        _("User Email"), unique=True, help_text=_("Unique email of the user"),
    )

    def __str__(self):
        return self.get_full_name()


class Post(models.Model):
    """
    Store the post data
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", help_text=_("The User who create the post")
    )
    title = models.CharField(_("Post Title"), max_length=100, help_text=_("The title of the post"))
    content = models.TextField(_("Post Content"), help_text=_("The content of the post"))
    file = models.FileField(
        upload_to='post_files/', blank=True, null=True, help_text=_("The file of the post")
    )
    created_at = models.DateTimeField(
        _("Post Created Date"), auto_now_add=True, help_text=_("The created date for the post")
    )

    def __str__(self):
        return self.title
