from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
      #----------------------------- admin thesis project manage url -----------------------
      #----------------------- thesis type ----------------------
      path('admin_create_thesis_type',views.create_thesis_type,name='admin_create_thesis_type'),
      path('admin_manage_thesis_type', views.manage_thesis_type, name='admin_manage_thesis_type'),
      path('admin_update_thesis_type/<id>', views.update_thesis_type, name='admin_update_thesis_type'),
      path('admin_delete_thesis_type/<id>', views.delete_thesis_type, name='admin_delete_thesis_type'),

      #----------------------- project type ----------------------
      path('admin_create_project_type',views.create_project_type, name='admin_create_project_type'),
      path('admin_manage_project_type', views.manage_project_type, name='admin_manage_project_type'),
      path('admin_update_project_type/<id>', views.update_project_type, name='admin_update_project_type'),
      path('admin_delete_project_type/<id>', views.delete_project_type, name='admin_delete_project_type'),

      # ----------------------- department ----------------------
      path('admin_create_department', views.create_department, name='admin_create_department'),
      path('admin_manage_department', views.manage_department, name='admin_manage_department'),
      path('admin_update_department/<id>', views.update_department, name='admin_update_department'),
      path('admin_delete_department/<id>', views.delete_department, name='admin_delete_department'),

      #-------------------------- thesis project -------------------------
      path('create_admin_thesis_project',views.create_admin_thesis_project,name='create_admin_thesis_project'),
      path('manage_admin_thesis_project',views.manage_admin_thesis_project,name='manage_admin_thesis_project'),
      path('pdf_show_admin/<id>',views.pdf_show_admin,name='pdf_show_admin'),
      path('admin_thesis_project_status/<id>', views.admin_thesis_project_status, name='admin_thesis_project_status'),
      path('admin_thesis_project_delete/<id>', views.admin_thesis_project_delete, name='admin_thesis_project_delete'),
      path('admin_thesis_project_update/<id>', views.admin_thesis_project_update, name='admin_thesis_project_update'),

      # ----------------------------- student thesis project manage url -----------------------
      path('create_student_thesis_project', views.create_student_thesis_project, name='create_student_thesis_project'),
      path('manage_student_thesis_project', views.manage_student_thesis_project, name='manage_student_thesis_project'),
      path('pdf_show_student/<id>', views.pdf_show_student, name='pdf_show_student'),

      # ----------------------------- teacher thesis project manage url -----------------------
      path('create_teacher_thesis_project', views.create_teacher_thesis_project, name='create_teacher_thesis_project'),
      path('manage_teacher_thesis_project', views.manage_teacher_thesis_project, name='manage_teacher_thesis_project'),
      path('pdf_show_teacher/<id>', views.pdf_show_teacher, name='pdf_show_teacher'),
      path('teacher_thesis_project_status/<id>', views.teacher_thesis_project_status, name='teacher_thesis_project_status'),
      path('teacher_thesis_project_update/<id>', views.teacher_thesis_project_update, name='teacher_thesis_project_update'),
      path('teacher_thesis_project_delete/<id>', views.teacher_thesis_project_delete, name='teacher_thesis_project_delete'),



    ]