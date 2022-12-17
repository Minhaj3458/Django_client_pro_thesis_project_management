from django import forms
from auth_dashboard_App.models import User
from .import models
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class Student_ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Student_profile
        fields = "__all__"