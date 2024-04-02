from django.urls import path
from . import views
from .schemas import schema_view


urlpatterns = [
    path('companies/', views.CompanyListAPIView.as_view(), name='company-list'),
    path('companies/<uuid:pk>/', views.CompanyDetailAPIView.as_view(), name='company-detail'),
    path('assets/', views.AssetListAPIView.as_view(), name='asset-list'),
    path('assets/<uuid:pk>/', views.AssetDetailAPIView.as_view(), name='asset-detail'),
    path('employees/', views.EmployeeListAPIView.as_view(), name='employee-list'),
    path('employees/<uuid:pk>/', views.EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('asset-assignments/', views.AssetAssignmentListAPIView.as_view(), name='asset-assignment-list'),
    path('asset-assignments/<uuid:pk>/', views.AssetAssignmentDetailAPIView.as_view(), name='asset-assignment-detail'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
