from django import forms
from .models import Pilot
from .models import LogbookEntry


class PilotForm(forms.ModelForm):
    class Meta:
        model = Pilot
        fields = [
            'first_name', 
            'middle_name',
            'last_name',
            'last_name' ,
            'date_of_birth' ,
            'gender',
            'phone',
            'email',
            'address1' ,
            'address2',
            'city',
            'state',
            'zipcode',
            'country',
        ]