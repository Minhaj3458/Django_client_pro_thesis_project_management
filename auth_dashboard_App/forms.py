from django import forms
from .import models
class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"

class Admin_ProfileForm(forms.ModelForm):
    class Meta:
        model = models.auth_profile_customer
        fields = "__all__"