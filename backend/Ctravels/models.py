from datetime import datetime
from turtle import position

from django.db import models


# Create your models here.

class Employees(models.Model):
    id_no = models.IntegerField(max_length=20, unique=True, null=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    mobile_no = models.CharField(max_length=50, unique=True, null=False)
    address = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    department = models.CharField(max_length=100, null=False)
    position = models.CharField(max_length=100, null=False)
    role = models.CharField(max_length=50, null=False)
    date_of_birth = models.DateField()
    date_of_hire = models.DateField()
    gender = models.CharField(max_length=10)
    public_service_no = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f'{self.first_name}  {self.last_name}  {self.mobile_no}  {self.id_no}  {self.email}'


class Departments(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'departments'

    def __str__(self):
        return f'{self.name}'


class Vehicles(models.Model):
    number_plate = models.CharField(max_length=50, primary_key=True)
    type = models.CharField(max_length=100, null=False)
    manufacturer = models.CharField(max_length=100, null=False)
    model = models.CharField(max_length=100, null=False)
    license_no = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=500, null=False)
    year = models.DateField()
    current_millage = models.CharField(max_length=100, null=False)
    last_service_date = models.DateField()
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    class Meta:
        db_table = 'vehicles'

    def __str__(self):
        return f'{self.number_plate}  {self.type}  {self.model}  {self.department}'


class Driver(models.Model):
    employee_id = models.ForeignKey(Employees, primary_key=True, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicles, on_delete=models.CASCADE)

    class Meta:
        db_table = 'driver'

    def __str__(self):
        return f'{self.employee_id}  {self.vehicle_id}'


class Mechanics(models.Model):
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    Address = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mechanics'

    def __str__(self):
        return f'{self.employee_id}  {self.first_name},  {self.last_name},  {self.mobile_no}'


class Repair(models.Model):
    vehicle_id = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    date = models.DateField()
    desc = models.TextField(max_length=500)
    cost = models.FloatField(null=True, blank=True)
    status = models.BooleanField(default=False)
    mechanic_id = models.ForeignKey(Mechanics, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'repairs'

    def __str__(self):
        return f'{self.vehicle_id}  {self.date}  {self.cost}  {self.status}'


class Maintenance(models.Model):
    vehicle_id = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    date = models.DateField()
    cost = models.FloatField()
    status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'maintenance'

    def __str__(self):
        return f'{self.vehicle_id}  {self.type}  {self.date}  {self.cost}  {self.status}'


class FuelStations(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    fuel_received = models.FloatField()
    fuel_sold = models.FloatField()
    fuel_remaining = models.FloatField()

    class Meta:
        db_table = 'fuel stations'

    def __str__(self):
        return f'{self.name}  {self.fuel_remaining}'


class FuelVendors(models.Model):
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE, primary_key=True)
    fuel_station = models.ForeignKey(FuelStations, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_info = models.TextField(max_length=255)
    unit_price = models.FloatField(default=0)
    total_fuel = models.FloatField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'fuel vendors'

    def __str__(self):
        return f'{self.name}  {self.fuel_station}  {self.unit_price}'


class StationFuelRefill(models.Model):
    name = models.CharField(max_length=100)
    vendor_id = models.ForeignKey(FuelVendors, on_delete=models.CASCADE)
    fuel_station = models.ForeignKey(FuelStations, on_delete=models.CASCADE)
    fuel_remaining = models.FloatField(default=0)
    fuel_received = models.FloatField(default=0)
    date_received = models.DateField()
    received_by = models.CharField(max_length=100)
    unit_price = models.FloatField(default=0)
    buying_cost = models.FloatField(default=0)

    class Meta:
        db_table = 'station fuel refill'

    def __str__(self):
        return f'{self.name}  {self.received_by}  {self.unit_price}  {self.buying_cost}'


class VehicleFuelRefill(models.Model):
    date = models.DateField()
    description = models.TextField(max_length=255)
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    fuel_station = models.ForeignKey(FuelStations, on_delete=models.CASCADE)
    unit_price = models.FloatField()
    total_cost = models.FloatField()
    issued_by = models.ForeignKey(FuelVendors, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'vehicles fuel refill'

    def __str__(self):
        return f'{self.first_name}'


class DriversFuelOrders(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'drivers fuel orders'

    def __str__(self):
        return f'{self.created_at}  {self.vehicle}  {self.status}  {self.description}'


class Notifications(models.Model):
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=100)
    notification_message = models.TextField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notifications'

    def __str__(self):
        return f'{self.notification_message}  {self.notification_type}  {self.is_read}  {self.created_at}  {self.employee_id}'