from django.contrib import admin
from .models import *

# Register all models in the admin site
for model in [
    StartPoint, EndPoint, MediaFile, ActivityCategory, ActivityType,
    Site, Equipment, Employee, EmployeeOne, EmployeeTwo, EmployeeThree,
    EmployeeFour, EmployeeFive, EmployeeSix, EmployeeSeven, EmployeeEight,
    EmployeeNine, EmployeeTen, EmployeeEleven, EmployeeTwelve,
    EmployeeThirteen, EmployeeFourteen, EmployeeFifteen, MyDateForm
]:
    admin.site.register(model)
