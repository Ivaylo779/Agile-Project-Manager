from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from tasks.models import Task, Label


class TaskBaseForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["created_at", "updated_at"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": 3}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "priority": forms.Select(attrs={"class": "form-control"}),
            }

        error_messages = {
            "title": {
                "required": "Please enter a task name.",
                "max_length": "The name can be at most 100 characters.",
                "min_length": "The name cannot be less than 3 characters.",
            },
            "description": {
                "max_length": "The goal can be at most 500 characters.",
            },
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")

        if title.isdigit():
            raise ValidationError("The task title cannot consist only of digits.")

        return title

class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "color": forms.TextInput(
                attrs={"type": "color", "class": "form-control form-control-color"}
                ),
            }

        error_messages = {
            "name": {
                "required": "Please enter a label name.",
                "max_length": "The name can be at most 100 characters.",
                "min_length": "The name cannot be less than 3 characters.",
            },
            "color": {
                "required": "Please enter a label color.",
            },
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if name.isdigit():
            raise ValidationError("The label name cannot consist only of digits.")

        return name


class TaskCreateForm(TaskBaseForm):
    ...


class TaskUpdateForm(TaskBaseForm):
    ...