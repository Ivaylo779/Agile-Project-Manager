from django import forms
from django.core.exceptions import ValidationError

from agile_project_manager.forms import BaseForm
from sprints.models import Sprint


class SprintBaseForm(BaseForm):
    class Meta:
        model = Sprint
        fields = '__all__'
        labels = {
            "name": "Sprint name",
            "start_date": "Start date",
            "end_date": "Planned end date",
        }
        help_texts = {
            "name": "At least 4 characters, not only digits.",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter a name..."}),
            "goal": forms.Textarea(attrs={"rows": 3}),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            }

        error_messages = {
            "name": {
                "required": "Please enter a sprint name.",
                "max_length": "The name can be at most 100 characters.",
                "min_length": "The name cannot be less than 4 characters.",
            },
            "goal": {
                "max_length": "The goal can be at most 100 characters.",
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
            raise ValidationError("The sprint name cannot consist only of digits.")

        return name


class SprintCreateForm(SprintBaseForm):
    ...


class SprintUpdateForm(SprintBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["project"].disabled = True