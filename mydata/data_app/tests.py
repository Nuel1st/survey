from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import MyModel  # Import your model
from .forms import (
    StartPointForm, EndPointForm, ActivitytypeForm, EquipmentForm, SiteForm,
    ActivitycategoryForm, EmployeeForm, Employee_role_Form, My_dateForm,
    Employee_one_Form, Employee_two_Form, Employee_three_Form, Employee_four_Form,
    Employee_five_Form, Employee_six_Form, Employee_seven_Form, Employee_eight_Form,
    Employee_nine_Form, Employee_ten_Form, Employee_eleven_Form, Employee_twelve_Form,
    Employee_thirteen_Form, Employee_fourteen_Form, Employee_fifteen_Form,
    Machinery_driver_name_Form,
)
from .serializers import MyModelSerializer
from django.test import RequestFactory

class MyModelViewTest(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.sample_data = {
            'field1': 'Sample Data 1',
            'field2': 'Sample Data 2',
            # ... other fields ...
        }
    
    def test_create_mymodel(self):
        # Ensure that a POST request to create a MyModel object works as expected
        url = reverse('submit_data')  # Replace with your actual URL name
        response = self.client.post(url, self.sample_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MyModel.objects.count(), 1)
        self.assertEqual(MyModel.objects.get().field1, 'Sample Data 1')

    # Add more test cases as needed

class HomeViewTest(TestCase):
    def setUp(self):
        # Create form instances for testing
        self.startpoint_form_data = {
            'startpoint_form': 'Start Data',
            # ... other fields ...
        }
        self.endpoint_form_data = {
            'endpoint_form': 'End Data',
            # ... other fields ...
        }
       
        self.factory = RequestFactory()
    
    def test_home_view_get(self):

        url = reverse('home')  
        request = self.factory.get(url)
        response = home(request)

        self.assertEqual(response.status_code, 200)
        
    
    def test_home_view_post(self):
        
        url = reverse('home')  # Replace with your actual URL name
        request = self.factory.post(url, data=self.startpoint_form_data)
        response = home(request)

        self.assertEqual(response.status_code, 200)  # You can adjust the expected status code
    

    # Add more test cases as needed
