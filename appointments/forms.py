from django import forms
import datetime
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    datetime = forms.DateField(initial=datetime.date.today)
    description = forms.CharField(label="Description")
    class Meta:
        model = Appointment
        fields = ('datetime', 'description',)
