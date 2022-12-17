from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    #-------------account---------------#
    path('student_reg',views.student_reg, name="student_reg"),
    path('student_login',views.student_login, name="student_login"),
    path('student_logout', views.student_logout, name="student_logout"),
    #------------------reset password---------------------------
     path("reset/password/",auth_views.PasswordResetView.as_view(template_name='views/student/account/password/password_reset.html'), name="password_reset"),
     path('reset/password/done/', auth_views.PasswordResetDoneView.as_view(template_name='views/student/account/password/password_reset_done.html'), name='password_reset_done'),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="views/student/account/password/password_reset_confirm.html"), name='password_reset_confirm'),
     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='views/student/account/password/password_reset_complete.html'), name='password_reset_complete'),

    #--------------------- home page -------------#
    path('student_home',views.home, name="student_home"),

    # --------------------- student profile -------------#
    path('stu_profile_show', views.stu_profile_show, name="stu_profile_show"),
    path('stu_profile_update/<id>', views.stu_profile_update, name="stu_profile_update"),
    path('manage_student',views.manage_student, name="manage_student"),
    path('stu_info_delete/<id>',views.stu_info_delete, name="stu_info_delete"),


    ]