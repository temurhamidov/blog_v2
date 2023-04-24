"""blog2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.authtoken.views import obtain_auth_token

schema_view = get_schema_view(
    openapi.Info(
        title='Blog web-site API',
        description='DRFni urganish uchun blogapi loyihasi',
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('user/', include('user.urls')),
    path('api/', include('myapp.api.urls')),
    path('api/user/', include('user.api.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('api-auth-token/', obtain_auth_token, name='obtain_auth_token'),
    path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger_url'),
    path('redocs', schema_view.with_ui('redoc', cache_timeout=0), name='schema_redoc_url'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler403='myapp.views.error_403'
handler404='myapp.views.error_404'

