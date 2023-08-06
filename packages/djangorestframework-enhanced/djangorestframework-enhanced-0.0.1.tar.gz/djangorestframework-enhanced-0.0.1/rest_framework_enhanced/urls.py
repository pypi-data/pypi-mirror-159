from django.urls import path, include
from django.conf import urls, settings
from django.views import debug
from rest_framework_enhanced.exceptions import handler_404, handler_500
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('jwt/login/', TokenObtainPairView.as_view(), name='jwt_token_login'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_token_refresh'),
]

if settings.API_ENHANCED.get('USE_CUSTOM_ERROR_PAGE'):
    urls.handler404 = handler_404
    debug.technical_404_response = handler_404
    urls.handler500 = handler_500
    debug.technical_500_response = handler_500
