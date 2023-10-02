from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from api.views import UserViewSet, PostViewSet, LogoutAPIView

app_name = "user_api"

router = SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register("post", PostViewSet, basename="users")

urlpatterns = router.urls

urlpatterns += [
    path("logout/", LogoutAPIView.as_view(), name="logout"),
]
