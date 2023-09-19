from django.db import models


class StartPoint(models.Model):
    start_point_chainage = models.PositiveIntegerField(verbose_name="Start Point Chainage")
    location = models.URLField(verbose_name="Share a Location (Map)")
    photo = models.ImageField(verbose_name="Share Start Point Photo", upload_to='start_point_photos/', blank=True, null=True)

    def __str__(self):
        return f"Start Point - Chainage: {self.start_point_chainage}"

# Model for End Point
class EndPoint(models.Model):
    end_point_chainage = models.PositiveIntegerField(verbose_name="End Point Chainage")
    location = models.URLField(verbose_name="Share a Location (Map)")
    photo = models.ImageField(verbose_name="Share End Point Photo", upload_to='end_point_photos/', blank=True, null=True)

    def __str__(self):
        return f"End Point - Chainage: {self.end_point_chainage}"

# Model for Media File
class MediaFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media_files/')

    def __str__(self):
        return self.title



# Model for Activity Category
class ActivityCategory(models.Model):
    category = models.CharField(max_length=255, verbose_name="Activity Category")

    def __str__(self):
        return self.category

# Model for Activity Type
class ActivityType(models.Model):
    category = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, verbose_name="Activity Type")

    def __str__(self):
        return self.type

# Model for Site
class Site(models.Model):
    site = models.CharField(max_length=255, verbose_name="Site")

    def __str__(self):
        return self.site

# Model for Equipment
class Equipment(models.Model):
    equipment = models.CharField(max_length=255, verbose_name="Equipment")

    def __str__(self):
        return self.equipment

# Model for Employee
class Employee(models.Model):
    employee = models.CharField(max_length=255, verbose_name="Employee")

    def __str__(self):
        return self.employee

# Model for Employee One
class EmployeeOne(models.Model):
    employee_one = models.CharField(max_length=255, verbose_name="Employee One")

    def __str__(self):
        return self.employee_one

class MyDateForm(models.Model):
    my_date = models.DateField(verbose_name="My Date")

    def __str__(self):
        return str(self.my_date)
    
class EmployeeOne(models.Model):
    employee_one = models.CharField(max_length=255, verbose_name="Employee One")

    def __str__(self):
        return self.employee_one
    
class EmployeeTwo(models.Model):
    employee_two = models.CharField(max_length=255, verbose_name="Employee Two")

    def __str__(self):
        return self.employee_two
    
class EmployeeThree(models.Model):
    employee_three = models.CharField(max_length=255, verbose_name="Employee Three")

    def __str__(self):
        return self.employee_three

class EmployeeFour(models.Model):
    employee_four = models.CharField(max_length=255, verbose_name="Employee Four")

    def __str__(self):
        return self.employee_four

class EmployeeFive(models.Model):
    employee_five = models.CharField(max_length=255, verbose_name="Employee Five")

    def __str__(self):
        return self.employee_five
    
class EmployeeSix(models.Model):
    employee_six = models.CharField(max_length=255, verbose_name="Employee Six")

    def __str__(self):
        return self.employee_six
    
class EmployeeSix(models.Model):
    employee_six = models.CharField(max_length=255, verbose_name="Employee Six")

    def __str__(self):
        return self.employee_six
    
class EmployeeSeven(models.Model):
    employee_seven = models.CharField(max_length=255, verbose_name="Employee Seven")

    def __str__(self):
        return self.employee_seven
    
class EmployeeEight(models.Model):
    employee_eight = models.CharField(max_length=255, verbose_name="Employee Eight")

    def __str__(self):
        return self.employee_eight
    
class EmployeeNine(models.Model):
    employee_nine = models.CharField(max_length=255, verbose_name="Employee Nine")

    def __str__(self):
        return self.employee_nine

class EmployeeTen(models.Model):
    employee_ten = models.CharField(max_length=255, verbose_name="Employee Ten")

    def __str__(self):
        return self.employee_ten

class EmployeeEleven(models.Model):
    employee_eleven = models.CharField(max_length=255, verbose_name="Employee Eleven")

    def __str__(self):
        return self.employee_eleven
    
class EmployeeTwelve(models.Model):
    employee_twelve = models.CharField(max_length=255, verbose_name="Employee Twelve")

    def __str__(self):
        return self.employee_twelve
    
class EmployeeThirteen(models.Model):
    employee_thirteen = models.CharField(max_length=255, verbose_name="Employee Thirteen")

    def __str__(self):
        return self.employee_thirteen
    
class EmployeeFourteen(models.Model):
    employee_fourteen = models.CharField(max_length=255, verbose_name="Employee Fourteen")

    def __str__(self):
        return self.employee_fourteen
    
class EmployeeFifteen(models.Model):
    employee_fiftteen = models.CharField(max_length=255, verbose_name="Employee Fifteen")

    def __str__(self):
        return self.employee_fiftteen