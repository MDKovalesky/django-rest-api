from django.urls import path, include
from rest_framework import routers


from api.views.users import UsersViewsSet
from api.views.register import RegisterSerializer

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'users', UsersViewsSet)

urlspattern = [
    path('', include(router.urls)),
    path('register/', RegisterSerializer.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
