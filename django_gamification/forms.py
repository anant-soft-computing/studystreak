from django import forms
from .models import BadgeDefinition

class BadgeDefinitionForm(forms.ModelForm):
    class Meta:
        model = BadgeDefinition
        fields = '__all__'
        widgets = {
            #'next_badge': forms.Select(),  # Use a regular select input for next_badge field
        }
