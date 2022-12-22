from django.shortcuts import render
from thesis_project_manage_App.models import Thesis_project_manage,Thesis_type,Project_type,Department
from django.core.paginator import Paginator
from auth_dashboard_App.models import Contact
from django.contrib import messages
import random
# Create your views here.

#----------------- home page --------------
def home(request):
    thesis_project =Thesis_project_manage.objects.filter(status=1).order_by('?')
    page = Paginator(thesis_project, 14)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    thesis_project_latest = Thesis_project_manage.objects.filter(status=1).order_by('-id')[:20]
    thesis_type = Thesis_type.objects.all().order_by('-id')
    project_type = Project_type.objects.all().order_by('-id')
    department = Department.objects.all().order_by('-id')
    context = {
        'thesis_project': page,
        'thesis_project_latest': thesis_project_latest,
        'thesis_type':thesis_type,
        'project_type':project_type,
        'department':department,
    }
    return render(request,'views/frontend/page/home.html',context)

#----------------- single page  thesis project details show--------------
def single_page(request,id):
    thesis_project = Thesis_project_manage.objects.get(id=id)
    thesis_project_latest = Thesis_project_manage.objects.filter(status=1).order_by('-id')[:10]
    thesis_type = Thesis_type.objects.all().order_by('-id')
    project_type = Project_type.objects.all().order_by('-id')
    department = Department.objects.all().order_by('-id')
    context ={
        'thesis_project':thesis_project,
        'thesis_project_latest': thesis_project_latest,
        'thesis_type': thesis_type,
        'project_type': project_type,
        'department': department,
    }
    return render(request, 'views/frontend/page/single_page_show.html',context)

#----------------- thesis type show-----------------
def thesis_type(request,id):
    thesis_project = Thesis_project_manage.objects.filter(thesis_type_id=id,status=1).order_by('?')
    page = Paginator(thesis_project, 14)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    thesis_project_latest = Thesis_project_manage.objects.filter(status=1).order_by('-id')[:20]
    thesis_type = Thesis_type.objects.all().order_by('-id')
    project_type = Project_type.objects.all().order_by('-id')
    department = Department.objects.all().order_by('-id')
    context = {
        'thesis_project': page,
        'thesis_project_latest': thesis_project_latest,
        'thesis_type': thesis_type,
        'project_type': project_type,
        'department': department,
    }
    return render(request,'views/frontend/page/thesis_type.html',context)


#----------------- department show-----------------
def department(request,id):
    thesis_project = Thesis_project_manage.objects.filter(department_id=id,status=1).order_by('?')
    page = Paginator(thesis_project, 14)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    thesis_project_latest = Thesis_project_manage.objects.filter(status=1).order_by('-id')[:20]
    thesis_type = Thesis_type.objects.all().order_by('-id')
    project_type = Project_type.objects.all().order_by('-id')
    department = Department.objects.all().order_by('-id')
    context = {
        'thesis_project': page,
        'thesis_project_latest': thesis_project_latest,
        'thesis_type': thesis_type,
        'project_type': project_type,
        'department': department,
    }
    return render(request,'views/frontend/page/department.html',context)

#----------------- project type -----------------
def project_type(request,id):
    thesis_project = Thesis_project_manage.objects.filter(project_type=id,status=1).order_by('?')
    page = Paginator(thesis_project, 14)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    thesis_project_latest = Thesis_project_manage.objects.filter(status=1).order_by('-id')[:20]
    thesis_type = Thesis_type.objects.all().order_by('-id')
    project_type = Project_type.objects.all().order_by('-id')
    department = Department.objects.all().order_by('-id')
    context = {
        'thesis_project': page,
        'thesis_project_latest': thesis_project_latest,
        'thesis_type': thesis_type,
        'project_type': project_type,
        'department': department,
    }
    return render(request,'views/frontend/page/project_type.html',context)



#----------------- contact page -----------------
def contact_page(request):
    thesis_project_latest = Thesis_project_manage.objects.filter(status=1).order_by('-id')[:20]
    thesis_type = Thesis_type.objects.all().order_by('-id')
    project_type = Project_type.objects.all().order_by('-id')
    department = Department.objects.all().order_by('-id')
    context = {
        'thesis_project_latest': thesis_project_latest,
        'thesis_type': thesis_type,
        'project_type': project_type,
        'department': department,
    }
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message')
        saves = contact.save()
        messages.success(request, 'Message Send Successfully!')
    return render(request,'views/frontend/page/contact.html',context)