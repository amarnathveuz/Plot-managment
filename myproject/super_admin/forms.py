from django import forms
 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
 
from .models import intractive_map

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = intractive_map
        fields =[ 'Name','Phoneno','UnitNo','BlockNo','UnitArea','LandArea' ,'UType','Price',
                  'Bank','Status'
        ] 