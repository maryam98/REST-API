from django import forms
from django.forms import fields
from django.forms.widgets import DateInput
from task.models import TodoTask

class DataInput(forms.DateInput):
    input_type='date'

class TaskCreatedForm(forms.ModelForm):
    created=forms.DateField(widget=DateInput)
    class Meta:
        model=TodoTask
        fields=('title','content','created','Category')

