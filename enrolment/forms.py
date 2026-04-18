from django import forms
from .models import Enrolment


class EnrolmentForm(forms.ModelForm):
    class Meta:
        model = Enrolment
        fields = ["student", "course", "semester", "year"]