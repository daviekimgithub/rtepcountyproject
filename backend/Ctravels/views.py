from rest_framework import generics

from .models import Employee, Driver, Mechanic, Department, Vehicle, Repair, Maintenance
from .models import FuelVendor, FuelStation
from .models import StationFuelRefill, DriversFuelOrder, VehicleFuelRefill, Notification
from .serializers import (
    EmployeeSerializer, DriverSerializer, MechanicSerializer, DepartmentSerializer,
    VehicleSerializer, RepairSerializer, MaintenanceSerializer, FuelVendorSerializer,
    FuelStationSerializer, StationFuelRefillSerializer, DriverFuelOrderSerializer,
    VehicleFuelRefillSerializer, NotificationSerializer
)


class EmployeesList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeesDetail(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DriversList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriversDetail(generics.RetrieveUpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class MechanicsList(generics.ListCreateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer


class MechanicsDetail(generics.RetrieveUpdateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer


class DepartmentsList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentsDetail(generics.RetrieveUpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class VehiclesList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehiclesDetail(generics.RetrieveUpdateAPIView):
    queryset = Vehicle.objects.all()
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
    queryset = FuelVendor.objects.all()
    serializer_class = FuelVendorSerializer


class FuelVendorsDetail(generics.RetrieveUpdateAPIView):
    queryset = FuelVendor.objects.all()
    serializer_class = FuelVendorSerializer


class FuelStationsList(generics.ListCreateAPIView):
    queryset = FuelStation.objects.all()
    serializer_class = FuelStationSerializer


class FuelStationsDetail(generics.RetrieveUpdateAPIView):
    queryset = FuelStation.objects.all()
    serializer_class = FuelStationSerializer


class StationFuelRefillList(generics.ListCreateAPIView):
    queryset = StationFuelRefill.objects.all()
    serializer_class = StationFuelRefillSerializer


class StationFuelRefillDetail(generics.RetrieveUpdateAPIView):
    queryset = StationFuelRefill.objects.all()
    serializer_class = StationFuelRefillSerializer


class DriversFuelOrdersList(generics.ListCreateAPIView):
    queryset = DriversFuelOrder.objects.all()
    serializer_class = DriverFuelOrderSerializer


class DriversFuelOrdersDetail(generics.RetrieveUpdateAPIView):
    queryset = DriversFuelOrder.objects.all()
    serializer_class = DriverFuelOrderSerializer


class VehicleFuelRefillList(generics.ListCreateAPIView):
    queryset = VehicleFuelRefill.objects.all()
    serializer_class = VehicleFuelRefillSerializer


class VehicleFuelRefillDetail(generics.RetrieveUpdateAPIView):
    queryset = VehicleFuelRefill.objects.all()
    serializer_class = VehicleFuelRefillSerializer


class NotificationsList(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationsDetail(generics.RetrieveUpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
