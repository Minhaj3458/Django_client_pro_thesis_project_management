from django import forms
from .import models

class Thesis_project_update_forms(forms.ModelForm):
    class Meta:
        model = models.Thesis_project_manage
        fields = "__all__"


