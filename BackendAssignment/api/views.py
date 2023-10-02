from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Post
from api.permissions import IsPostOwner
from api.serializers import UserSerializer, PostSerializer
from utils.constants import USER_LOGOUT_SUCCESSFULLY, TOKEN_INVALID, REFRESH_TOKEN_NOT_PROVIDED

User = get_user_model()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ["retrieve", "update", "partial_update", "destroy"]:
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()

    def get_queryset(self):
        """
        return: only login user
        """
        return self.queryset.filter(email=self.request.user.email)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        refresh = RefreshToken.for_user(user)
        data["refresh"], data["access"] = str(refresh), str(refresh.access_token)
        return Response(data, status=status.HTTP_201_CREATED)


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, IsPostOwner)

    def get_queryset(self):
        """
        return: list of login user created post
        """
        return self.queryset.filter(user=self.request.user)


class LogoutAPIView(GenericAPIView):
    """
    User logout API
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response(REFRESH_TOKEN_NOT_PROVIDED, status=status.HTTP_400_BAD_REQUEST)
        try:
            data = RefreshToken(refresh_token)
            data.blacklist()
            return Response(USER_LOGOUT_SUCCESSFULLY, status=status.HTTP_200_OK)
        except TokenError:
            return Response(TOKEN_INVALID, status=status.HTTP_400_BAD_REQUEST)
