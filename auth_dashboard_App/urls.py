from django.urls import path
from .import views
urlpatterns = [
    #-------------- authentication--------------
    path('admin_reg',views.auth_reg, name="admin_reg"),
    path('admin_login',views.auth_login, name="admin_login"),
    path('admin_logout',views.auth_logout, name="admin_logout"),
    path('user_manage', views.user_manage, name="user_manage"),
    path('user_status/<id>', views.user_status, name="user_status"),
    path('user_delete/<id>', views.user_delete, name="user_delete"),

    #--------------------- profile -----------------
    path('create_admin_profile', views.create_admin_profile, name="create_admin_profile"),
    path('manage_admin_profile', views.manage_admin_profile, name="manage_admin_profile"),
    path('show_admin_profile', views.show_admin_profile, name="show_admin_profile"),
    path('update_admin_profile/<id>', views.update_admin_profile, name="update_admin_profile"),
    path('admin_profile_delete/<id>', views.admin_profile_delete, name="admin_profile_delete"),

    #--------------------- Home Page -----------------
    path('admin_home', views.home ,name="admin_home" ),

    # --------------------- Contact -----------------
    path('manage_contact', views.manage_contact, name="manage_contact"),
    path('delete_contact/<id>', views.delete_contact, name="delete_contact"),
    path('update_contact/<id>', views.update_contact, name="update_contact"),
    ]