from django import forms
from django.core.exceptions import ValidationError


class BaseForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")

        if end < start:
            raise ValidationError("Start date must be greater than end date.")

        return cleaned_data


