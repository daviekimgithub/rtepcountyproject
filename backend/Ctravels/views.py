from rest_framework import generics

from .models import Employees, Driver, Mechanics, Departments, Vehicles, Repair, Maintenance
from .models import FuelVendors, FuelStations
from .models import StationFuelRefill, DriversFuelOrders, VehicleFuelRefill, Notifications
from .serializers import (
    EmployeeSerializer, DriverSerializer, MechanicSerializer, DepartmentSerializer,
    VehicleSerializer, RepairSerializer, MaintenanceSerializer, FuelVendorSerializer,
    FuelStationSerializer, StationFuelRefillSerializer, DriverFuelOrderSerializer,
    VehicleFuelRefillSerializer, NotificationSerializer
)


class EmployeesList(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class EmployeesDetail(generics.RetrieveUpdateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class DriversList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriversDetail(generics.RetrieveUpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class MechanicsList(generics.ListCreateAPIView):
    queryset = Mechanics.objects.all()
    serializer_class = MechanicSerializer


class MechanicsDetail(generics.RetrieveUpdateAPIView):
    queryset = Mechanics.objects.all()
    serializer_class = MechanicSerializer


class DepartmentsList(generics.ListCreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentsDetail(generics.RetrieveUpdateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


class VehiclesList(generics.ListCreateAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer


class VehiclesDetail(generics.RetrieveUpdateAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer


class RepairList(generics.ListCreateAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer


class RepairDetail(generics.RetrieveUpdateAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer


class MaintenanceList(generics.ListCreateAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class MaintenanceDetail(generics.RetrieveUpdateAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class FuelVendorsList(generics.ListCreateAPIView):
    queryset = FuelVendors.objects.all()
    serializer_class = FuelVendorSerializer


class FuelVendorsDetail(generics.RetrieveUpdateAPIView):
    queryset = FuelVendors.objects.all()
    serializer_class = FuelVendorSerializer


class FuelStationsList(generics.ListCreateAPIView):
    queryset = FuelStations.objects.all()
    serializer_class = FuelStationSerializer


class FuelStationsDetail(generics.RetrieveUpdateAPIView):
    queryset = FuelStations.objects.all()
    serializer_class = FuelStationSerializer


class StationFuelRefillList(generics.ListCreateAPIView):
    queryset = StationFuelRefill.objects.all()
    serializer_class = StationFuelRefillSerializer


class StationFuelRefillDetail(generics.RetrieveUpdateAPIView):
    queryset = StationFuelRefill.objects.all()
    serializer_class = StationFuelRefillSerializer


class DriversFuelOrdersList(generics.ListCreateAPIView):
    queryset = DriversFuelOrders.objects.all()
    serializer_class = DriverFuelOrderSerializer


class DriversFuelOrdersDetail(generics.RetrieveUpdateAPIView):
    queryset = DriversFuelOrders.objects.all()
    serializer_class = DriverFuelOrderSerializer


class VehicleFuelRefillList(generics.ListCreateAPIView):
    queryset = VehicleFuelRefill.objects.all()
    serializer_class = VehicleFuelRefillSerializer


class VehicleFuelRefillDetail(generics.RetrieveUpdateAPIView):
    queryset = VehicleFuelRefill.objects.all()
    serializer_class = VehicleFuelRefillSerializer


class NotificationsList(generics.ListCreateAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer


class NotificationsDetail(generics.RetrieveUpdateAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
