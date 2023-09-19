from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from django.views import View
from .forms import ActivitytypeForm, EquipmentForm, SiteForm, ActivitycategoryForm, EmployeeForm, Employee_role_Form, Machinery_driver_name_Form, My_dateForm, Employee_one_Form, Employee_two_Form, Employee_three_Form, Employee_four_Form, Employee_five_Form, Employee_six_Form, Employee_seven_Form, Employee_eight_Form, Employee_nine_Form, Employee_ten_Form, Employee_eleven_Form, Employee_twelve_Form, Employee_thirteen_Form, Employee_fourteen_Form, Employee_fifteen_Form
from .forms import MediaFileForm, StartPointForm, EndPointForm  # Import the MediaFileForm
import base64
from django.contrib import messages



def home(request):
    current_time = timezone.now()
    selected_activitytype = None
    selected_activitycategory =None
    selected_equipment = None
    selected_site = None
    selected_employee = None
    selected_employee_role = None
    selected_machinery_driver_name = None
    selected_my_date = None
    selected_employee_one = None
    selected_employee_two = None
    selected_employee_three = None
    selected_employee_four = None
    selected_employee_five = None
    selected_employee_six = None
    selected_employee_seven = None
    selected_employee_eight = None
    selected_employee_nine = None
    selected_employee_ten = None
    selected_employee_eleven = None
    selected_employee_twelve = None
    selected_employee_thirteen = None
    selected_employee_fourteen = None
    selected_employee_fifteen = None



    if request.method == 'POST':
        activitytype_form = ActivitytypeForm(request.POST)
        equipment_form = EquipmentForm(request.POST)
        site_form = SiteForm(request.POST)
        activitycategory_form = ActivitycategoryForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        employee_role_form = Employee_role_Form(request.POST)
        machinery_driver_name_form = Machinery_driver_name_Form(request.POST)
        my_date_form = My_dateForm(request.POST)
        employee_one_form = Employee_one_Form(request.POST)
        employee_two_form = Employee_two_Form(request.POST)
        employee_three_form = Employee_three_Form(request.POST)
        employee_four_form = Employee_four_Form(request.POST)
        employee_five_form = Employee_five_Form(request.POST)
        employee_six_form = Employee_six_Form(request.POST)
        employee_seven_form = Employee_seven_Form(request.POST)
        employee_eight_form = Employee_eight_Form(request.POST)
        employee_nine_form = Employee_nine_Form(request.POST)
        employee_ten_form = Employee_ten_Form(request.POST)
        employee_eleven_form = Employee_eleven_Form(request.POST)
        employee_twelve_form = Employee_twelve_Form(request.POST)
        employee_thirteen_form = Employee_thirteen_Form(request.POST)
        employee_fourteen_form = Employee_fourteen_Form(request.POST)
        employee_fifteen_form = Employee_fifteen_Form(request.POST)

    
        
        if activitytype_form.is_valid() and equipment_form.is_valid() and site_form.is_valid() and activitycategory_form.is_valid() and employee_form.is_valid() and employee_role_form and my_date_form.is_valid and employee_one_form() and employee_two_form() and employee_three_form and employee_four_form() and employee_five_form() and employee_six_form() and employee_seven_form() and employee_eight_form() and employee_nine_form() and employee_ten_form() and employee_eleven_form and employee_twelve_form() and employee_thirteen_form() and employee_fourteen_form() and employee_fifteen_form :
            selected_activitytype = activitytype_form.cleaned_data['activity']
            selected_equipment = equipment_form.cleaned_data['equipment']
            selected_site = site_form.cleaned_data['site']
            selected_activitycategory = activitycategory_form['activitycategory']
            selected_employee =activitycategory_form['employee']
            selected_employee_role = employee_role_form['employee_role']
            selected_machinery_driver_name = Machinery_driver_name_Form['machinery_driver_name']
            selected_my_date = my_date_form.cleaned_data['date'] 
            selected_employee_one = employee_one_form.cleaned_data['employee_one']
            selected_employee_two = employee_two_form.cleaned_data['employee_two']
            selected_employee_three = employee_three_form.cleaned_data['employee_three']
            selected_employee_four = employee_four_form.cleaned_data['employee_four']
            selected_employee_five = employee_five_form.cleaned_data['employee_five']
            selected_employee_six = employee_six_form.cleaned_data['employee_six']
            selected_employee_seven = employee_seven_form.cleaned_data['employee_seven']
            selected_employee_eight = employee_eight_form.cleaned_data['employee_eight']
            selected_employee_nine = employee_nine_form.cleaned_data['employee_nine']
            selected_employee_ten = employee_ten_form.cleaned_data['employee_ten']
            selected_employee_eleven = employee_eleven_form.cleaned_data['employee_eleven']
            selected_employee_twelve = employee_twelve_form.cleaned_data['employee_twelve']
            selected_employee_thirteen = employee_thirteen_form.cleaned_data['employee_thirteen']
            selected_employee_fourteen = employee_fourteen_form.cleaned_data['employee_one']
            selected_employee_fifteen = employee_fifteen_form.cleaned_data['employee_one']


            # You can now use 'selected_activity' and 'selected_equipment' as needed.

    else:
        activitytype_form = ActivitytypeForm()
        equipment_form = EquipmentForm()
        site_form = SiteForm()
        activitycategory_form= ActivitycategoryForm()
        employee_form= EmployeeForm()
        employee_role_form= Employee_role_Form()
        machinery_driver_name_form= Machinery_driver_name_Form()
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


   
    return render(request, 'home.html', {
    'current_time': current_time,
    'activitytype_form': activitytype_form,
    'equipment_form': equipment_form,
    'site_form': site_form,
    'activitycategory_form': activitycategory_form,
    'employee_form': employee_form,
    'employee_role_form': employee_role_form,
    'machinery_driver_name_form': machinery_driver_name_form,
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
    'employee_fifiteen_form': employee_fifteen_form,
    'selected_activitytype': selected_activitytype,
    'selected_equipment': selected_equipment,
    'selected_site': selected_site,
    'selected_activitycategory': selected_activitycategory,
    'selected_employee': selected_employee,
    'selected_emmployee_role': selected_employee_role,
    'selected_machinery_driver_name': selected_machinery_driver_name,
    'selected_my_date': selected_my_date,
    'selected_employee_one': selected_employee_one,
    'selected_employee_two': selected_employee_two,
    'selected_employee_three': selected_employee_three,
    'selected_employee_four': selected_employee_four,
    'selected_employee_five': selected_employee_five,
    'selected_employee_six': selected_employee_six,
    'selected_employee_seven': selected_employee_seven,
    'selected_employee_eight': selected_employee_eight,
    'selected_employee_nine': selected_employee_nine,
    'selected_employee_ten': selected_employee_ten,
    'selected_employee_eleven': selected_employee_eleven,
    'selected_employee_twelve': selected_employee_twelve,
    'selected_employee_thirteen': selected_employee_thirteen,
    'selected_employee_fourteen': selected_employee_fourteen,
    'selected_employee_fifteen': selected_employee_fifteen
})


def upload_media(request):
    if request.method == 'POST':
        media_form = MediaFileForm(request.POST, request.FILES)
        if media_form.is_valid():
            # Save the form data to the database
            media_instance = media_form.save()

            # Optionally, encode the file to base64 if needed
            uploaded_file = media_instance.file
            base64_data = ''
            with uploaded_file.open('rb') as file:
                base64_data = base64.b64encode(file.read()).decode()

            messages.success(request, 'Media file uploaded successfully.')

            return redirect('upload_success')  # Redirect to a success page

    else:
        media_form = MediaFileForm()

    return render(request, 'media.html', {'media_form': media_form})


def create_start_point(request):
    if request.method == 'POST':
        form = StartPointForm(request.POST, request.FILES)
        if form.is_valid():
            request.session['start_point_data'] = {
                'chainage': form.cleaned_data['start_point_chainage'],  # Correct field name
                'location': form.cleaned_data['location'],
                'photo': form.cleaned_data['photo'].url if form.cleaned_data['photo'] else None,
            }
            messages.success(request, 'Start Point created successfully.')
            return redirect('success_page')
    else:
        form = StartPointForm()

    return render(request, 'start_point.html', {'start_form': form})


 


def create_end_point(request):
    if request.method == 'POST':
        form = EndPointForm(request.POST, request.FILES)
        if form.is_valid():
            request.session['end_point_data'] = {
                'chainage': form.cleaned_data['chainage'],
                'location': form.cleaned_data['location'],
                'photo': form.cleaned_data['photo'].url if form.cleaned_data['photo'] else None,
            }
            messages.success(request, 'End Point created successfully.')
            return redirect('success_page')
    else:
        form = EndPointForm()

    return render(request, 'end_point.html', {'end_form': form})



def success_page(request):

    start_point_data = request.session.get('start_point_data', None)
    if start_point_data:
        return render(request, 'success_page.html', {'start_point_data': start_point_data})
    else:
        return HttpResponse('No start point data found.')


        


# from django.shortcuts import render, redirect
# from .forms import ActivityCategoryForm, ActivityTypeForm

# def your_view_name_here(request):
#     if request.method == 'POST':
#         activity_category_form = ActivityCategoryForm(request.POST)
#         activity_type_form = ActivityTypeForm(request.POST)

#         if activity_category_form.is_valid() and activity_type_form.is_valid():
#             activity_category = activity_category_form.cleaned_data['activity_category']
#             activity_type = activity_type_form.cleaned_data['activity_type']

#             # Save activity_category and activity_type to the database or perform other actions here

#             # Redirect or render a success page
#             return redirect('success_page_url')  # Replace 'success_page_url' with the actual URL

#     else:
#         activity_category_form = ActivityCategoryForm()
#         activity_type_form = ActivityTypeForm()

#     return render(request, 'your_template_name.html', {
#         'activity_category_form': activity_category_form,
#         'activity_type_form': activity_type_form,
#     })

