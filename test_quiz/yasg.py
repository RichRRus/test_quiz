from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Quiz API',
        default_version='v1',
        description='Documentation for quiz api v1',
        license=openapi.License(name='MIT License', url='https://opensource.org/licenses/MIT'),
    ),
    public=True,
    url='http://localhost:8000/api/v1/',
    authentication_classes=()
)


urlpatterns = [
    path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'), # noqa
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
