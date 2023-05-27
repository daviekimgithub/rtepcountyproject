from rest_framework import serializers
from .models import Employee, Driver, Mechanic, Department, Vehicle, Repair, Maintenance
from .models import FuelVendor, FuelStation
from .models import StationFuelRefill, DriversFuelOrder, VehicleFuelRefill, Notification


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
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
        model = Department
        fields = ('pk', 'name', 'created_at', 'updated_at')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
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
            'created_at',
            'updated_at',
        )


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = (
            'pk',
            'employee_id',
            'vehicle_id',
            'created_at',
            'updated_at',
        )


class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = (
            'pk',
            'employee_id',
            'first_name',
            'last_name',
            'mobile_no',
            'gender',
            'Address',
            'created_at',
            'updated_at',
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
            'created_at',
            'updated_at',
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
            'created_at',
            'updated_at',
        )


class FuelStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelStation
        fields = (
            'name',
            'description',
            'fuel_received',
            'fuel_sold',
            'fuel_remaining',
            'created_at',
            'updated_at',
        )


class FuelVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelVendor
        fields = (
            'employee_id',
            'fuel_station',
            'name',
            'contact_info',
            'unit_price',
            'total_fuel',
            'created_at',
            'updated_at',
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
            'created_at',
            'updated_at',
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
            'created_at',
            'updated_at',
        )


class DriverFuelOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriversFuelOrder
        fields = (
            'driver',
            'vehicle',
            'description',
            'status',
            'created_at',
            'updated_at',
        )


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'employee_id',
            'notification_type',
            'notification_message',
            'is_read',
            'created_at',
            'updated_at',
        )
