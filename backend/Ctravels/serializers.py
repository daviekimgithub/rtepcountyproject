from rest_framework import serializers
from .models import Employees, Driver, Mechanics, Departments, Vehicles, Repair, Maintenance
from .models import FuelVendors, FuelStations
from .models import StationFuelRefill, DriversFuelOrders, VehicleFuelRefill, Notifications


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = (
            'pk',
            'id_no',
            'first_name',
            'last_name',
            'mobile_no',
            'address',
            'email',
            'department',
            'position',
            'role',
            'date_of_birth',
            'date_of_hire',
            'gender',
            'public_service_no',
            'created_at',
            'updated_at',
        )


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('pk', 'name')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = (
            'number_plate',
            'type',
            'manufacturer',
            'model',
            'license_no',
            'description',
            'year',
            'current_millage',
            'last_service_date',
            'department',
        )


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = (
            'pk',
            'employee_id',
            'vehicle_id',
        )


class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanics
        fields = (
            'pk',
            'employee_id',
            'first_name',
            'last_name',
            'mobile_no',
            'gender',
            'Address',
            'created_on',
            'updated_on',
        )


class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = (
            'vehicle_id',
            'date',
            'desc',
            'cost',
            'status',
            'mechanic_id',
            'created_on',
            'updated_on',
        )


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = (
            'vehicle_id',
            'type',
            'date',
            'cost',
            'status',
            'created_on',
            'updated_on',
        )


class FuelStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelStations
        fields = (
            'name',
            'description',
            'fuel_received',
            'fuel_sold',
            'fuel_remaining',
        )


class FuelVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelVendors
        fields = (
            'employee_id',
            'fuel_station',
            'name',
            'contact_info',
            'unit_price',
            'total_fuel',
            'created_on',
            'updated_on',
        )


class StationFuelRefillSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationFuelRefill
        fields = (
            'name',
            'vendor_id',
            'fuel_station',
            'fuel_remaining',
            'fuel_received',
            'date_received',
            'received_by',
            'unit_price',
            'buying_cost',
        )


class VehicleFuelRefillSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleFuelRefill
        fields = (
            'date',
            'description',
            'vehicle',
            'fuel_station',
            'unit_price',
            'total_cost',
            'issued_by',
            'driver',
            'status',
        )


class DriverFuelOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriversFuelOrders
        fields = (
            'created_on',
            'updated_on',
            'driver',
            'vehicle',
            'description',
            'status',
        )


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = (
            'employee_id',
            'notification_type',
            'notification_message',
            'is_read',
            'created_at',
        )
