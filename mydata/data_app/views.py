from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .forms import StartPointForm, EndPointForm, ActivitytypeForm, EquipmentForm, SiteForm, ActivitycategoryForm, EmployeeForm, Employee_role_Form, My_dateForm, Employee_one_Form, Employee_two_Form, Employee_three_Form, Employee_four_Form, Employee_five_Form, Employee_six_Form, Employee_seven_Form, Employee_eight_Form, Employee_nine_Form, Employee_ten_Form, Employee_eleven_Form, Employee_twelve_Form, Employee_thirteen_Form, Employee_fourteen_Form, Employee_fifteen_Form, Machinery_driver_name_Form, MediaFileForm
from .forms import MediaFileForm, StartPointForm, EndPointForm  # Import the MediaFileForm
import base64
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import MyModel
from .serializers import MyModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# def api(request, url):
# EndPoint= "http://localhost:8300/api"


context = {}
context['processing_form'] = False



def user_data(request, user_id):
    # Assuming you have a unique field like 'user_id' in your model
    data = get_object_or_404(MyModel, user_id=2)  # Replace 'user_id' with your actual field name

    return render(request, 'base/user_data.html', {'data': data})

def gate(request):
    names and aallForm()
    if forms.is_valid:
        return home


def home(request):
    # Initialize form instances
    startpoint_form = StartPointForm()
    endpoint_form = EndPointForm()
    activitytype_form = ActivitytypeForm()
    equipment_form = EquipmentForm()
    site_form = SiteForm()
    activitycategory_form = ActivitycategoryForm()
    employee_form = EmployeeForm()
    employee_role_form = Employee_role_Form()
    my_date_form = My_dateForm()
    employee_one_form = Employee_one_Form()
    employee_two_form = Employee_two_Form()
    employee_three_form = Employee_three_Form()
    employee_four_form = Employee_four_Form()
    employee_five_form = Employee_five_Form()
    employee_six_form = Employee_six_Form()
    employee_seven_form = Employee_seven_Form()
    employee_eight_form = Employee_eight_Form()
    employee_nine_form = Employee_nine_Form()
    employee_ten_form = Employee_ten_Form()
    employee_eleven_form = Employee_eleven_Form()
    employee_twelve_form = Employee_twelve_Form()
    employee_thirteen_form = Employee_thirteen_Form()
    employee_fourteen_form = Employee_fourteen_Form()
    employee_fifteen_form = Employee_fifteen_Form()
    machinery_driver_name_form = Machinery_driver_name_Form()
    mediafile_form = MediaFileForm()

    # Retrieve existing data
    all_data = MyModel.objects.all()

    context = {
        'startpoint_form': startpoint_form,
        'endpoint_form': endpoint_form,
        'activitytype_form': activitytype_form,
        'equipment_form': equipment_form,
        'site_form': site_form,
        'activitycategory_form': activitycategory_form,
        'employee_form': employee_form,
        'employee_role_form': employee_role_form,
        'my_date_form': my_date_form,
        'employee_one_form': employee_one_form,
        'employee_two_form': employee_two_form,
        'employee_three_form': employee_three_form,
        'employee_four_form': employee_four_form,
        'employee_five_form': employee_five_form,
        'employee_six_form': employee_six_form,
        'employee_seven_form': employee_seven_form,
        'employee_eight_form': employee_eight_form,
        'employee_nine_form': employee_nine_form,
        'employee_ten_form': employee_ten_form,
        'employee_eleven_form': employee_eleven_form,
        'employee_twelve_form': employee_twelve_form,
        'employee_thirteen_form': employee_thirteen_form,
        'employee_fourteen_form': employee_fourteen_form,
        'employee_fifteen_form': employee_fifteen_form,
        'machinery_driver_name_form': machinery_driver_name_form,
        'all_data': all_data,
        'mediafile_form': mediafile_form
    }

    return render(request, 'base/home.html', context)

@api_view(['POST'])
def submit_data(request):
    if request.method == 'POST':
        # Process each form individually and save data
        startpoint_form = StartPointForm(request.data)
        endpoint_form = EndPointForm(request.data)
        activitytype_form = ActivitytypeForm(request.data)
        equipment_form = EquipmentForm(request.data)
        site_form = SiteForm(request.data)
        activitycategory_form = ActivitycategoryForm(request.data)
        employee_form = EmployeeForm(request.data)
        employee_role_form = Employee_role_Form(request.data)
        my_date_form = My_dateForm(request.data)
        employee_one_form = Employee_one_Form(request.data)
        employee_two_form = Employee_two_Form(request.data)
        employee_three_form = Employee_three_Form(request.data)
        employee_four_form = Employee_four_Form(request.data)
        employee_five_form = Employee_five_Form(request.data)
        employee_six_form = Employee_six_Form(request.data)
        employee_seven_form = Employee_seven_Form(request.data)
        employee_eight_form = Employee_eight_Form(request.data)
        employee_nine_form = Employee_nine_Form(request.data)
        employee_ten_form = Employee_ten_Form(request.data)
        employee_eleven_form = Employee_eleven_Form(request.data)
        employee_twelve_form = Employee_twelve_Form(request.data)
        employee_thirteen_form = Employee_thirteen_Form(request.data)
        employee_fourteen_form = Employee_fourteen_Form(request.data)
        employee_fifteen_form = Employee_fifteen_Form(request.data)
        machinery_driver_name_form = Machinery_driver_name_Form(request.data)
        mediafile_form = MediaFileForm(request.data)

        if (
            startpoint_form.is_valid() and endpoint_form.is_valid() and
            activitytype_form.is_valid() and equipment_form.is_valid() and
            site_form.is_valid() and activitycategory_form.is_valid() and
            employee_form.is_valid() and employee_role_form.is_valid() and
            my_date_form.is_valid() and employee_one_form.is_valid() and
            employee_two_form.is_valid() and employee_three_form.is_valid() and
            employee_four_form.is_valid() and employee_five_form.is_valid() and
            employee_six_form.is_valid() and employee_seven_form.is_valid() and
            employee_eight_form.is_valid() and employee_nine_form.is_valid() and
            employee_ten_form.is_valid() and employee_eleven_form.is_valid() and
            employee_twelve_form.is_valid() and employee_thirteen_form.is_valid() and
            employee_fourteen_form.is_valid() and employee_fifteen_form.is_valid()
            and machinery_driver_name_form.is_valid() and mediafile_form.is_valid()
        ):
            # Save the data to the database using your serializer
            serializer = MyModelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                messages.success(request, 'Form data submitted successfully.')

                # Redirect to the home page after saving
                return redirect('home')
            else:
                # Handle serializer errors
                messages.error(request, 'Error submitting form data.')
        else:
            # Handle form validation errors
            messages.error(request, 'Form validation errors. Please check the form fields.')

    return Response({"message": "Invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def all_data(request):
    data = MyModel.objects.all()  # Retrieve all objects from the database
    return render(request, 'base/all_data.html', {'data': data})

def upload_media(request):
    if request.method == 'POST':
        media_form = MediaFileForm(request.POST, request.FILES)
        if media_form.is_valid():
            request.session['processing_form'] = True
            context['loading'] = True

            # context['loading'] = True
            # Save the form data to the database
            media_form = media_form.save()

            # Optionally, encode the file to base64 if needed
            uploaded_file = media_instance.file
            base64_data = ''
            with uploaded_file.open('rb') as file:
                base64_data = base64.b64encode(file.read()).decode() 

            messages.success(request, 'Media file uploaded successfully.')

            return redirect('upload_success')  # Redirect to a success page

    else:
        media_form = MediaFileForm()

    return render(request, 'base/media.html', {'media_form': media_form})

def create_start_point(request):
    if request.method == 'POST':
        start_form = StartPointForm(request.POST, request.FILES)
        if start_form.is_valid():
            context['loading'] = True
            request.session['start_point_data'] = {
                'chainage': start_form.cleaned_data['chainage'],
                'location': start_form.cleaned_data['location'],
                'photo': start_form.cleaned_data['photo'].url if start_form.cleaned_data['photo'] else None,
            }
            messages.success(request, 'Start Point created successfully.')
            return redirect('upload_success')
            
    else:
        start_form = StartPointForm()

    return render(request, 'base/start_point.html', {'start_form': start_form})

def create_end_point(request):
    if request.method == 'POST':
        end_form = EndPointForm(request.POST, request.FILES)
        if end_form.is_valid():
            context['loading'] = True
            request.session['end_point_data'] = {
                'chainage': form.cleaned_data['chainage'],
                'location': form.cleaned_data['location'],
                'photo': form.cleaned_data['photo'].url if end_form.cleaned_data['photo'] else None,
            }
            messages.success(request, 'End Point created successfully.')
            return redirect('success_page')
    else:
        end_form = EndPointForm()

    return render(request, 'base/end_point.html', {'end_form': end_form})

def success_page(request):
    start_point_data = request.session.get('start_point_data', None)
    if start_point_data:
        return render(request, 'base/success_page.html', {'start_point_data': start_point_data})
    else:
        return HttpResponse('No start point data found.')
