from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CreateUserApiView, UserApiView

urlpatterns = [
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('register/',CreateUserApiView.as_view(), name='user_register'),
        path('user/<id>/',UserApiView.as_view(), name='user_update')

]
