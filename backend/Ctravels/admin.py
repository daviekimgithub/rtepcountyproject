from django.contrib import admin
from .models import Employee, Driver, Mechanic, Department, Vehicle, Repair, Maintenance
from .models import FuelVendor, FuelStation
from .models import StationFuelRefill, DriversFuelOrder, VehicleFuelRefill, Notification


# Register your models here.
admin.site.register(Employee)
admin.site.register(Driver)
admin.site.register(Mechanic)
admin.site.register(Department)
admin.site.register(Vehicle)
admin.site.register(Repair)
admin.site.register(Maintenance)
admin.site.register(FuelVendor)
admin.site.register(FuelStation)
admin.site.register(StationFuelRefill)
admin.site.register(DriversFuelOrder)
admin.site.register(VehicleFuelRefill)
admin.site.register(Notification)