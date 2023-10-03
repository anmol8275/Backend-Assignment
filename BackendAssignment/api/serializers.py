from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _

from api.models import Post
from utils.constants import PASSWORD_NOT_MATCH_ERROR, EMAIL_ALREADY_EXIST
from utils.utils import normalize_email, get_random_username

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    serializer for user
    """

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]
        extra_kwargs = {
            "username": {"read_only": True},
            "email": {"read_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate_password(self, password):
        validate_password(password=password)
        return password

    def validate(self, attrs):
        """
        Validation for user registration
        """
        password = attrs.get("password")
        confirm_password = attrs.pop("confirm_password", None)
        if password != confirm_password:
            raise serializers.ValidationError(
                {"password": [_(PASSWORD_NOT_MATCH_ERROR)]}
            )
        if attrs.get("email") and User.objects.filter(email=normalize_email(attrs.get("email"))).exists():
            raise serializers.ValidationError({"email": [_(EMAIL_ALREADY_EXIST)]})
        return attrs

    def create(self, validated_data):
        """
        Create the user
        """
        email = normalize_email(validated_data.pop("email"))
        random_username = get_random_username(email)
        user = User.objects.create_user(
            username=random_username, email=email, **validated_data
        )
        return user


class UserRegisterSerializer(UserSerializer):
    confirm_password = serializers.CharField(max_length=128, write_only=True, required=True)

    class Meta(UserSerializer.Meta):
        model = User
        fields = UserSerializer.Meta.fields + [
            "email",
            "password",
            "confirm_password"
        ]
        extra_kwargs = {
            "username": {"read_only": True},
            "password": {"write_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }


class PostSerializer(serializers.ModelSerializer):
    """
    serializer for post
    """

    class Meta:
        model = Post
        fields = ["id", "user", "title", "content", "file", "created_at"]
        extra_kwargs = {
            "user": {"read_only": True},
            "created_at": {"read_only": True}
        }

    def create(self, validated_data):
        """
        Create the post
        """
        return Post.objects.create(user=self.context.get("request").user, **validated_data)

    def to_representation(self, instance):
        ret = super(PostSerializer, self).to_representation(instance)
        user = User.objects.filter(id=ret.get("user")).first()
        ret["user"] = {"id": user.id, "email": user.email}
        return ret
