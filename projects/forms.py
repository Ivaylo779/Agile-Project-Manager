from django import forms
from django.core.exceptions import ValidationError

from agile_project_manager.forms import BaseForm
from projects.models import Project


class ProjectBaseForm(BaseForm):
    class Meta:
        model = Project
        exclude = ["created_at"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            }

        error_messages = {
            "name": {
                "required": "Please enter a project name.",
                "max_length": "The name can be at most 100 characters.",
                "min_length": "The name cannot be less than 2 characters.",
            },
            "description": {
                "max_length": "The description can be at most 500 characters.",
            },
            "start_date": {
                "required": "Choose a start date.",
                "invalid": "Enter a valid date.",
            },
            "end_date": {
                "required": "Choose a end date.",
                "invalid": "Enter a valid date.",
            }
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if name.isdigit():
            raise ValidationError("The project name cannot consist only of digits.")

        return name


class ProjectCreateForm(ProjectBaseForm):
    ...


class ProjectUpdateForm(ProjectBaseForm):
    ...

