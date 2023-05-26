from django.contrib import admin
from .models import Employees, Driver, Mechanics, Departments, Vehicles, Repair, Maintenance
from .models import FuelVendors, FuelStations
from .models import StationFuelRefill, DriversFuelOrders, VehicleFuelRefill, Notifications


# Register your models here.
admin.site.register(Employees)
admin.site.register(Driver)
admin.site.register(Mechanics)
admin.site.register(Departments)
admin.site.register(Vehicles)
admin.site.register(Repair)
admin.site.register(Maintenance)
admin.site.register(FuelVendors)
admin.site.register(FuelStations)
admin.site.register(StationFuelRefill)
admin.site.register(DriversFuelOrders)
admin.site.register(VehicleFuelRefill)
admin.site.register(Notifications)