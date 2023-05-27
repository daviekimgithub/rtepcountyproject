from django.urls import path
from . import views

urlpatterns = [
    path('api/employees/', views.EmployeesList.as_view()),
    path('api/employees/<str:pk>/', views.EmployeesDetail.as_view()),
    path('api/drivers/', views.DriversList.as_view()),
    path('api/drivers/<str:pk>/', views.DriversDetail.as_view()),
    path('api/mechanics/', views.MechanicsList.as_view()),
    path('api/mechanics/<str:pk>/', views.MechanicsDetail.as_view()),
    path('api/departments/', views.DepartmentsList.as_view()),
    path('api/departments/<str:pk>/', views.DepartmentsDetail.as_view()),
    path('api/vehicles/', views.VehiclesList.as_view()),
    path('api/vehicles/<str:pk>/', views.VehiclesDetail.as_view()),
    path('api/repairs/', views.RepairList.as_view()),
    path('api/repairs/<str:pk>/', views.RepairDetail.as_view()),
    path('api/maintenance/', views.MaintenanceList.as_view()),
    path('api/maintenance/<str:pk>/', views.MaintenanceDetail.as_view()),
    path('api/fuelvendors/', views.FuelVendorsList.as_view()),
    path('api/fuelvendors/<str:pk>/', views.FuelVendorsDetail.as_view()),
    path('api/fuelstations/', views.FuelStationsList.as_view()),
    path('api/fuelstations/<str:pk>/', views.FuelStationsDetail.as_view()),
    path('api/stationfuelrefills/', views.StationFuelRefillList.as_view()),
    path('api/stationfuelrefills/<str:pk>/', views.StationFuelRefillDetail.as_view()),
    path('api/driversfuelorders/', views.DriversFuelOrdersList.as_view()),
    path('api/driversfuelorders/<str:pk>/', views.DriversFuelOrdersDetail.as_view()),
    # Add more URL patterns for the remaining models if needed
]
