from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CategoryViewSet, UserViewSet, ProductViewSet, ArtisanViewSet, CustomerViewSet
from .auth_views import register_user, login_user


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'artisan', ArtisanViewSet)
router.register(r'customer', CustomerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]