import uuid
from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=250)
    
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ('name',)

    def __str__(self):
        return self.name

class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True) 
    serial_number = models.CharField(max_length=200)
    purchase_date = models.DateField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="devices")
    condition = models.CharField(max_length=220, default="Good")
    checkout = models.BooleanField(default=False)
    asset_issued = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        ordering = ['serial_number',]
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)  # Add email field
    position = models.CharField(max_length=100)  # Add position field
    department = models.CharField(max_length=100)  # Add department field
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employees")
    assets = models.ManyToManyField(Asset)
    
    def __str__(self):
        return self.employee_name


class AssetAssignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Assingned_by = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='assignments')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee')
    updated_at = models.DateField(auto_now_add=True)
    assigned_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    return_notes = models.TextField()
    asset_issued = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'DeviceAssignment'
        ordering = ('-updated_at',)
        
    def __str__(self):
        return f"Assignment: {self.asset.name} to {self.employee.employee_name}"


