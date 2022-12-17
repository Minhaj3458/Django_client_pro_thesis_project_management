from django.db import models
from auth_dashboard_App.models import User
# Create your models here.
class Thesis_type(models.Model):
    thesis_type = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project_type(models.Model):
    project_type = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Department(models.Model):
    department_name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Thesis_project_manage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    thesis_type = models.ForeignKey(Thesis_type, on_delete=models.CASCADE, null=True, blank=True)
    project_type = models.ForeignKey(Project_type, on_delete=models.CASCADE, null=True, blank=True)
    topic_name = models.CharField(max_length=400)
    student_id = models.CharField(max_length=200, null=True, blank=True)
    teacher_id = models.CharField(max_length=200, null=True, blank=True)
    supervisor_name = models.CharField(max_length=200, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(blank=True, null=True, max_length=20)
    email = models.CharField(blank=True, null=True, max_length=100)
    submit_by = models.CharField(max_length=200)
    description = models.TextField(max_length=500, null=True, blank=True)
    status = models.BooleanField(default=False)
    pdf = models.FileField(upload_to='static/backend/pdf/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)