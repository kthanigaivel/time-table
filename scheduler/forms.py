from django import forms
from . models import TimeTable,Schedule


class TimePickerInput(forms.TimeInput):
    input_type = 'time'

class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields= '__all__'
        exclude = ['period_duration']
        widgets = {
            'period_start': TimePickerInput(),
            'period_end' : TimePickerInput()
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields= ['schedule']
  