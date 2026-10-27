from django import forms
from django.core.exceptions import ValidationError
from tasks.models import Task, Label


class TaskBaseForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["created_at", "updated_at"]
        labels = {
            "title": "Task title",
        }
        help_texts = {
            "title": "At least 3 characters, not only digits.",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter a title..."}),
            "description": forms.Textarea(attrs={"rows": 3}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "priority": forms.Select(attrs={"class": "form-control"}),
            }

        error_messages = {
            "title": {
                "required": "Please enter a task title.",
                "max_length": "The title can be at most 100 characters.",
                "min_length": "The title cannot be less than 3 characters.",
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

class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = "__all__"
        labels = {
            "name": "Label name",
        }
        help_texts = {
            "name": "At least 3 characters, not only digits.",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter a name..."}),
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["sprint"].disabled = True