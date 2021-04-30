from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        # extra information about the form
        model = Todo

        # field that can be edited in the form
        fields = ["name", "description", "due_date"]
