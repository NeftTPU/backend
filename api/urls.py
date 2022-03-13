from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path, re_path
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('images/', views.store_image),
    path('collections/', views.CollectionAPIView().as_view()),
    re_path(r'^collections/(?P<id>[0-9]+)$', views.CollectionAPIView.as_view()),
    path('layers/', views.LayerAPIView().as_view()),
    re_path(r'^layers/(?P<id>[0-9]+)$', views.LayerAPIView.as_view()),
    path('pools/', views.PoolListAPIView().as_view()),
    re_path(r'^pools/(?P<id>[0-9]+)$', views.PoolAPIView.as_view()),
]
