from django import forms
from .models import Measurement


class FormOfMeasurement(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = {'destination',}
