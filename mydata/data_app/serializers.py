from rest_framework import serializers
from .models import MyModel, StartPoint, EndPoint, MediaFile, ActivityCategory, ActivityType, Site, Equipment, Employee, MyDateForm, EmployeeOne, EmployeeTwo, EmployeeThree, EmployeeFour, EmployeeFive, EmployeeSix, EmployeeSeven, EmployeeEight, EmployeeNine, EmployeeTen, EmployeeEleven, EmployeeTwelve, EmployeeThirteen, EmployeeFourteen, EmployeeFifteen, Machinery_driver_name

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'

class StartPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartPoint
        fields = '__all__'

class EndPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndPoint
        fields = '__all__'

class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = '__all__'

class ActivityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = '__all__'

class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = '__all__'

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class MyDateFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyDateForm
        fields = '__all__'

class EmployeeOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeOne
        fields = '__all__'

class EmployeeTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTwo
        fields = '__all__'

class EmployeeThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeThree
        fields = '__all__'

class EmployeeFourSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeFour
        fields = '__all__'

class EmployeeFiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeFive
        fields = '__all__'

class EmployeeSixSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSix
        fields = '__all__'

class EmployeeSevenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSeven
        fields = '__all__'

class EmployeeEightSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeEight
        fields = '__all__'

class EmployeeNineSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeNine
        fields = '__all__'

class EmployeeTenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTen
        fields = '__all__'

class EmployeeElevenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeEleven
        fields = '__all__'

class EmployeeTwelveSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTwelve
        fields = '__all__'

class EmployeeThirteenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeThirteen
        fields = '__all__'

class EmployeeFourteenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeFourteen
        fields = '__all__'

class EmployeeFifteenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeFifteen
        fields = '__all__'

class MachineryDriverNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machinery_driver_name
        fields = '__all__'
