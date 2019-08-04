from django import forms
from todo_list.models import Todos
from todoapp import settings


class TodosForm(forms.ModelForm):
    todo_date_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )

    class Meta:
        model = Todos
        fields = ['title', 'description', 'status', 'todo_date_time']
