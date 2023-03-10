from django.urls import path, include

from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import RegisterView, UserViewSet

router = routers.SimpleRouter()

router.register(r"users", UserViewSet)

urlpatterns = [
    # API Auth
    path('', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('register/', RegisterView.as_view())
] + router.urls
