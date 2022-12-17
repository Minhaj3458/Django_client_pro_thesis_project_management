from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
     #-------------account---------------#
    path('teacher_reg',views.teacher_reg, name="teacher_reg"),
    path('teacher_login',views.teacher_login, name="teacher_login"),
    path('teacher_logout',views.teacher_logout, name="teacher_logout"),

    #-------------- profile -------------#
    path('teacher_profile',views.teacher_profile,name="teacher_profile"),
    path('update_teacher_profile/<id>',views.update_teacher_profile,name="update_teacher_profile"),
    path('manage_teacher_profile',views.manage_teacher_profile,name="manage_teacher_profile"),
    path('delete_teacher_profile/<id>',views.delete_teacher_profile,name="delete_teacher_profile"),

    #-------------- manage student -----------#
    path('teacher_manage_student',views.teacher_manage_student,name="teacher_manage_student"),
    path('student_status/<id>',views.student_status,name="student_status"),
    path('delete_student/<id>', views.delete_student,name="delete_student"),


    ]