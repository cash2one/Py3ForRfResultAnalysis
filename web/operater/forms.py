from django import forms
from django.forms import  ModelForm
from web.models import create_data
class databaseforms(forms.Form):
    name = forms.CharField(max_length=255)
    IP_Address = forms.TextInput()
    Port = forms.IntegerField(default=11)
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

    class Meta:
        model = create_data



