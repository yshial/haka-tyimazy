from django import forms

from .models import Event, Task, City, Person


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class TaskCreateForm(forms.ModelForm):
    accountable = PersonCreateForm()

    class Meta:
        model = Task
        fields = '__all__'


# class CityCreateForm(forms.ModelForm):
#     city_scale = forms.ChoiceField(choices=GEEKS_CHOICES)
#
#     class Meta:
#         model = City
#         fields = '__all__'
