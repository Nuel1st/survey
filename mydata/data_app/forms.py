from django import forms
from .models import StartPoint, EndPoint
from .models import MediaFile 
from .models import MyModel

# from leaflet.forms.widgets import LeafletWidget


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__' 


class My_dateForm(forms.Form):
    my_date = forms.DateField(
         widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'Select a datetime...'}),
        label='Select a date'
    )

# Start Point Form
class StartPointForm(forms.Form):
    start_point_chainage = forms.IntegerField(label='Start Point Chainage', widget=forms.NumberInput(attrs={'type': 'number'}))
    location = forms.CharField(label='Share Location', widget=forms.TextInput(attrs={'type': 'url'}))
    photo = forms.ImageField(label='Share Start Point Photo', required=False)

# End Point Form
class EndPointForm(forms.Form):
    end_point_chainage = forms.IntegerField(label='End Point Chainage', widget=forms.NumberInput(attrs={'type': 'number'}))
    location = forms.CharField(label='Share Location', widget=forms.TextInput(attrs={'type': 'url'}))
    photo = forms.ImageField(label='Share end Point Photo', required=False)


Activitycategory_CHOICES = [
    ('Survey_and_Design', 'Survey and Design'),
    ('Clearing_and_Grading', 'Clearing and Grading'),
    ('Setting_out_points', 'Setting out points'),
    ('Excavation_and_Earthwork', 'Excavation and Earthwork'),
    ('Subbase_Installation', 'Subbase Installation'),
    ('Base_Course_Installation', 'Base Course Installation'),
    ('Paving', 'Paving'),
    ('Construction_of_Drainage_Channels', 'Construction of Drainage Channels'),
    ('Sidewalks_and_Shoulders', 'Sidewalks and Shoulders'),
    ('Road_Markings_and_Signage', 'Road Markings and Signage'),
    ('Vegetation_and_Landscaping', 'Vegetation and Landscaping'),
    ('Quality_Control_and_Inspection', 'Quality Control and Inspection'),
]

class ActivitycategoryForm(forms.Form):
    activitycategory = forms.ChoiceField(choices=Activitycategory_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

Activitytype_CHOICES = [
    ('', 'Select Activity type'),
    ('surveying of the area to determine road alignment, width…', 'surveying of the area to determine road alignment, width…'),
    ('Create detailed road design plans', 'Create detailed road design plans'),
    ('Clear the construction site of vegetation and obstacles', 'Clear the construction site of vegetation and obstacles'),
    ('Grade and prepare the roadbed to the required specifications', 'Grade and prepare the roadbed to the required specifications'),
    ('Road requirements boundary', 'Road requirements boundary'),
    ('Road requirements boundary', 'Road requirements boundary'),
    ('paving', 'Paving'),
    ('cut_and_fill_elevations', 'Cut and Fill Elevations'),
    ('excavate_roadbed', 'Excavate the Roadbed to the Required Depth and Width'),
    ('proper_compaction_subgrade', 'Ensure Proper Compaction of the Subgrade'),
    ('layer_subbase_material', 'Lay a Layer of Subbase Material'),
    ('compact_subbase', 'Compact Subbase to Provide Additional Stability and Drainage'),
    ('place_base_course_material', 'Place Base Course Material'),
    ('compact_base_course_material', 'Compact Base Course Material'),
    ('asphalt_or_concrete_surface', 'Apply an Asphalt or Concrete Surface Layer'),
    ('compact_surface_layer', 'Compact the Asphalt or Concrete Surface Layer'),
    ('excavate_drainage_channels', 'Excavate and Shape the Drainage Channels'),
    ('line_drainage_channels', 'Line Drainage Channels with Appropriate Materials'),
    ('install_culverts', 'Install Culverts or Cross-Drainage Structures'),
    ('construct_sidewalks_and_shoulders', 'Construct Sidewalks and Shoulders'),
    ('paint_road_markings', 'Paint Road Markings (Lane Lines, Crosswalks, Arrows)'),
    ('install_traffic_signs_and_signals', 'Install Traffic Signs and Signals'),
    ('plant_grass_or_vegetation', 'Plant Grass or Vegetation to Prevent Erosion'),
    ('implement_landscaping_elements', 'Implement Landscaping Elements to Beautify'),
    ('ensure_compliance_with_standards', 'Ensure Compliance with Design Specifications and Safety Standards'),
    ('quality_control_tests', 'Conduct Quality Control Tests on Materials, Compaction, and Pavement Thickness'),
]

class ActivitytypeForm(forms.Form):
    # Search_activity_type = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search...'}))
    activitytype = forms.ChoiceField(choices=Activitytype_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


SITE_CHOICES =(
    ('AKUWZU', 'AWKUZU'),
    ('ASABA', 'ASABA')
)
    
class SiteForm(forms.Form):
    site = forms.ChoiceField(choices=SITE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EQUIPMENT_CHOICES = [
    ('', 'Select an Equipment'),
    ('Dozer', 'Dozer'),
    ('Grader', 'Grader'),
    ('Excavator', 'Excavator'),
    ('Smooth_Roller', 'Smooth Roller'),
    ('Padfoot_Roller', 'Padfoot Roller'),
    ('Water_Tanker', 'Water Tanker'),
    ('Diesel_Tanker', 'Diesel Tanker'),
    ('Hillux_Pickup', 'Hillux Pickup'),
    ('Level_Instruments', 'Level Instruments'),
    ('Total_Stations', 'Total Stations'),
    ('Vehicles', 'Vehicles'),
    ('Containers', 'Containers'),
]

class EquipmentForm(forms.Form):
    equipment = forms.ChoiceField(choices=EQUIPMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # equipment = forms.ChoiceField(choices=EQUIPMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))



EMPLOYEE_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class EmployeeForm(forms.Form):
    employee = forms.ChoiceField(choices=EMPLOYEE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

EMPLOYEE_ONE_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_one_Form(forms.Form):
    employee_one = forms.ChoiceField(choices=EMPLOYEE_ONE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EMPLOYEE_TWO_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_two_Form(forms.Form):
    employee_two = forms.ChoiceField(choices=EMPLOYEE_TWO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EMPLOYEE_THREE_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_three_Form(forms.Form):
    employee_three = forms.ChoiceField(choices=EMPLOYEE_THREE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EMPLOYEE_FOUR_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_four_Form(forms.Form):
    employee_four = forms.ChoiceField(choices=EMPLOYEE_FOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EMPLOYEE_FIVE_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_five_Form(forms.Form):
    employee_five = forms.ChoiceField(choices=EMPLOYEE_FIVE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EMPLOYEE_SIX_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_six_Form(forms.Form):
    employee_six = forms.ChoiceField(choices=EMPLOYEE_SIX_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EMPLOYEE_SEVEN_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_seven_Form(forms.Form):
    employee_seven = forms.ChoiceField(choices=EMPLOYEE_SEVEN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EMPLOYEE_EIGHT_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_eight_Form(forms.Form):
    employee_eight = forms.ChoiceField(choices=EMPLOYEE_EIGHT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))



EMPLOYEE_NINE_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_nine_Form(forms.Form):
    employee_nine = forms.ChoiceField(choices=EMPLOYEE_NINE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EMPLOYEE_TEN_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_ten_Form(forms.Form):
    employee_ten = forms.ChoiceField(choices=EMPLOYEE_TEN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EMPLOYEE_ELEVEN_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]


class Employee_eleven_Form(forms.Form):
    employee_eleven = forms.ChoiceField(choices=EMPLOYEE_ELEVEN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EMPLOYEE_TWELVE_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_twelve_Form(forms.Form):
    employee_twelve = forms.ChoiceField(choices=EMPLOYEE_TWELVE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EMPLOYEE_THIRTEEN_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_thirteen_Form(forms.Form):
    employee_thirteen = forms.ChoiceField(choices=EMPLOYEE_THIRTEEN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EMPLOYEE_FOURTEEN_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_fourteen_Form(forms.Form):
    employee_fourteen = forms.ChoiceField(choices=EMPLOYEE_FOURTEEN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


EMPLOYEE_FIFTEEN_CHOICES = [
    ('', 'Select an employee'),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Employee_fifteen_Form(forms.Form):
    employee_fifteen = forms.ChoiceField(choices=EMPLOYEE_FIFTEEN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))




MACHINERY_DRIVER_NAME_CHOICES= [
    ('', 'Select the Machinery dirver name '),
    ('Andy_Okon', 'Andy Okon'),
    ('Awuhe_Apollos', 'Awuhe Apollos'),
    ('Benjamin', 'Benjamin'),
    ('Ebuka_Igbalo', 'Ebuka Igbalo'),
    ('Favor_Ugagbe', 'Favor Ugagbe'),
    ('Felix_Isebemhe', 'Felix Isebemhe'),
    ('Ibrahim_Dollar', 'Ibrahim Dollar'),
    ('Ikemaka_Chibuzor', 'Ikemaka Chibuzor'),
    ('Ime_Sunday', 'Ime Sunday'),
    ('Jonathan', 'Jonathan'),
    ('Kenneth_Nnamdi', 'Kenneth Nnamdi'),
    ('Lamas_Aminu', 'Lamas Aminu'),
    ('Manasseh_Tine', 'Manasseh Tine'),
    ('Nathaniel_Irehovbude', 'Nathaniel Irehovbude'),
    ('Ozugwor_Rufus', 'Ozugwor Rufus'),
    ('Patrick_Terhele', 'Patrick Terhele'),
    ('Peter_Uwadia', 'Peter Uwadia'),
    ('Richard', 'Richard'),
    ('Security', 'Security'),
    ('Sidi_Adaba', 'Sidi Adaba'),
    ('Tunde_Iyodo', 'Tunde Iyodo'),
    ('Tyokumba_Terfa', 'Tyokumba Terfa'),
    ('Usman_Tairu', 'Usman Tairu'),
    ('Yahya_Moussa', 'Yahya Moussa'),
]

class Machinery_driver_name_Form(forms.Form):
    machinery_driver_name = forms.ChoiceField(choices=MACHINERY_DRIVER_NAME_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))



EMPLOYEE_ROLE_CHOICES = [
    ('', 'Select Employee Role'),
    ('PRO', 'PRO'),
    ('Surveyor', 'Surveyor'),
    ('Chain_Boy', 'Chain Boy'),
    ('Excavator_Operator', 'Excavator Operator'),
    ('Dozer_Operator', 'Dozer Operator'),
    ('Driver', 'Driver'),
    ('Securities', 'Securities'),
    ('Forman', 'Forman'),
    ('Roller_Operator', 'Roller Operator'),
    ('Mechanic', 'Mechanic'),
    ('Electrician', 'Electrician'),
    ('Grader_Operator', 'Grader Operator'),
]

class Employee_role_Form(forms.Form):
    employee_role = forms.ChoiceField(choices=EMPLOYEE_ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))



class MediaFileForm(forms.Form):
    title = forms.CharField(max_length=255)
    file = forms.FileField()




# class MediaFileForm(forms.ModelForm):
#     class Meta:
#         model = MediaFile
#         fields = ['title', 'file']




# class StartPointForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

# class EndPointForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


# class StartPointForm(forms.ModelForm):
#     class Meta:
#         model = StartPoint
#         fields = ['chainage', 'location', 'title', 'location_lat', 'location_lon', 'photo']

# class EndPointForm(forms.ModelForm):
#     class Meta:
#         model = EndPoint
#         fields = ['chainage', 'location', 'title', 'location_lat', 'location_lon', 'photo']
