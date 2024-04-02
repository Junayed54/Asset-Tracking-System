from django.contrib import admin
from .models import Company, Asset, Employee, AssetAssignment

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'company', 'condition', 'checkout', 'asset_issued')
    search_fields = ('name', 'serial_number', 'company__name')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'email', 'position', 'department', 'company')
    search_fields = ('employee_name', 'email', 'position', 'department', 'company__name')

@admin.register(AssetAssignment)
class AssetAssignmentAdmin(admin.ModelAdmin):
    list_display = ('asset', 'employee', 'assigned_date', 'return_date', 'asset_issued')
    search_fields = ('asset__name', 'employee__employee_name', 'assigned_date', 'return_date')
