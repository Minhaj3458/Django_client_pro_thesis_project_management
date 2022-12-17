from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    #------------------- home page ----------------
    path('',views.home,name='home'),
    # ------------------- single page details show ----------------
    path('single_page/<id>', views.single_page, name='single_page'),

    # ------------------- thesis type  ----------------
    path('thesis_type/<id>', views.thesis_type, name='thesis_type'),

    # ------------------- thesis type  ----------------
    path('department/<id>', views.department, name='department'),

   # ------------------- project type  ----------------
    path('project_type/<id>', views.project_type, name='project_type'),

    # ------------------- contact page ----------------
    path('contact_page', views.contact_page, name='contact_page'),
    ]