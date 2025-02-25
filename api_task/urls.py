from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="Auth API",
        default_version='v1',
        description="API for user authentication",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="krisna.pranav@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')), 
    path('', TemplateView.as_view(template_name='index.html'), name='frontend'),  
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-auth/', include('rest_framework.urls')),  
]