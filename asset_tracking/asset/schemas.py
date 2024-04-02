from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
       title="Asset Tracking API",
       default_version='v1',
       description="API documentation for Asset Tracking application",
       terms_of_service="https://www.example.com/policies/terms/",
       contact=openapi.Contact(email="contact@example.com"),
       license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


