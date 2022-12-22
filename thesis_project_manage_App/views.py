from django.shortcuts import render,redirect
from .import models,forms
import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
#------------------------------------ admin manage thesis type -------------------

#------------------------------ create thesis type ---------------------------------
@login_required(login_url='admin_login')
def create_thesis_type(request):
    if request.method == 'POST':
        thesis_type_check = request.POST.get('thesis_type')
        if models.Thesis_type.objects.filter(thesis_type= thesis_type_check):
            thesis_type_error = 'This Thesis Type Already Exist'
            return render(request,'views/auth/dashboard/Thesis_type/create_thesis_type.html',
                          {'thesis_type_error': thesis_type_error })
        thesis_type = models.Thesis_type()
        thesis_type.thesis_type = thesis_type_check
        save = thesis_type.save()
        if not save:
            messages.success(request, 'This Thesis Type Create Successfully!')
            return redirect('admin_create_thesis_type')
        else:
            messages.success(request, 'Some Thing is wrong!')
            return redirect('admin_create_thesis_type')
    return render(request,'views/auth/dashboard/Thesis_type/create_thesis_type.html')

#------------------------- manage thesis Type ----------------
@login_required(login_url='admin_login')
def manage_thesis_type(request):
    Thesis_type = models.Thesis_type.objects.all().order_by('-id')
    context = {
        'Thesis_type': Thesis_type,
    }
    return render(request, 'views/auth/dashboard/Thesis_type/manage_thesis_type.html',context)
#------------------------- update thesis Type ---------------------
@login_required(login_url='admin_login')
def update_thesis_type(request,id):
    thesis_type = models.Thesis_type.objects.get(id=id)
    if request.method == 'POST':
        thesis_type.thesis_type = request.POST.get('thesis_type')
        save = thesis_type.save()
        if not save:
            messages.success(request, 'This Thesis Type Update Successfully!')
            return redirect('admin_manage_thesis_type')
        else:
            messages.success(request, 'Some Thing is wrong!')
            return redirect('admin_manage_thesis_type')
    context = {
        'Thesis_type': thesis_type,
    }
    return render(request, 'views/auth/dashboard/Thesis_type/update_thesis_type.html',context)
#------------------------- delete thesis Type ---------------------
@login_required(login_url='admin_login')
def delete_thesis_type(request,id):
    thesis_type = models.Thesis_type.objects.get(id=id)
    delete = thesis_type.delete()
    if delete:
        messages.success(request, 'This Thesis Type Delete Successfully!')
        return redirect('admin_manage_thesis_type')
    else:
        messages.success(request, 'Some Thing is wrong!')
        return redirect('admin_manage_thesis_type')

#------------------------------------ admin manage project type -------------------

#---------------- create project type --------------------------
@login_required(login_url='admin_login')
def create_project_type(request):
    project_type = models.Project_type()
    if request.method == 'POST':
        project_type_check = request.POST.get('project_type')
        if models.Project_type.objects.filter(project_type=project_type_check ):
            project_type_error = 'This Project Type Already Exist'
            return render(request, 'views/auth/dashboard/project_type/create_project_type.html',
                          {'project_type_error': project_type_error })
        project_type.project_type = project_type_check
        save = project_type.save()
        if not save:
            messages.success(request, 'This Project Type Create Successfully!')
            return redirect('admin_create_project_type')
        else:
            messages.success(request, 'Some Thing is wrong!')
            return redirect('admin_create_project_type')
    return render(request, 'views/auth/dashboard/project_type/create_project_type.html')

#---------------- manage project type --------------------------
@login_required(login_url='admin_login')
def manage_project_type(request):
    Project_type = models.Project_type.objects.all().order_by('-id')
    context = {
        'Project_type': Project_type,
    }
    return render(request, 'views/auth/dashboard/project_type/manage_project_type.html',context)

#---------------- update project type --------------------------
@login_required(login_url='admin_login')
def update_project_type(request,id):
    project_type = models.Project_type.objects.get(id=id)
    if request.method == 'POST':
        project_type.project_type = request.POST.get('project_type')
        save = project_type.save()
        if not save:
            messages.success(request, 'This Project Type Update Successfully!')
            return redirect('admin_manage_project_type')
        else:
            messages.success(request, 'Some Thing is wrong!')
            return redirect('admin_manage_project_type')
    context = {
        'Project_type': project_type,
    }
    return render(request, 'views/auth/dashboard/project_type/update_project_type.html',context)
#---------------- delete project type --------------------------
@login_required(login_url='admin_login')
def delete_project_type(request,id):
    project_type = models.Project_type.objects.get(id=id)
    delete = project_type.delete()
    if delete:
        messages.success(request, 'This Project Type Delete Successfully!')
        return redirect('admin_manage_project_type')
    else:
        messages.success(request, 'Some Thing is wrong!')
        return redirect('admin_manage_project_type')


#------------------------------------ admin manage department -------------------

#---------------- create department --------------------------
@login_required(login_url='admin_login')
def create_department(request):
    department = models.Department()
    if request.method == 'POST':
        department_type_check = request.POST.get('department_name')
        if models.Department.objects.filter(department_name=department_type_check):
            department_name_error = 'This Department Name Already Exist'
            return render(request,'views/auth/dashboard/department/create_department.html',
                          {'department_name_error': department_name_error})
        department.department_name = department_type_check
        save = department.save()
        if not save:
            messages.success(request, 'This Department Name  Create Successfully!')
            return redirect('admin_create_department')
        else:
            messages.success(request, 'Some Thing is wrong!')
            return redirect('admin_create_department')
    return render(request, 'views/auth/dashboard/department/create_department.html')

#---------------- manage department --------------------------
@login_required(login_url='admin_login')
def manage_department(request):
    Department = models.Department.objects.all().order_by('-id')
    context = {
        'Department': Department,
    }
    return render(request, 'views/auth/dashboard/department/manage_department.html',context)

#---------------- update department --------------------------
@login_required(login_url='admin_login')
def update_department(request,id):
    department = models.Department.objects.get(id=id)
    if request.method == 'POST':
        department.department_name = request.POST.get('department_name')
        save = department.save()
        if not save:
            messages.success(request, 'This Department Name Update Successfully!')
            return redirect('admin_manage_department')
        else:
            messages.success(request, 'Some Thing is wrong!')
            return redirect('admin_manage_department')
    context = {
        'Department': department,
    }
    return render(request, 'views/auth/dashboard/department/update_department.html',context)

#---------------- update department --------------------------
@login_required(login_url='admin_login')
def delete_department(request,id):
    department = models.Department.objects.get(id=id)
    delete = department.delete()
    if delete:
        messages.success(request, 'This Department Name Delete Successfully!')
        return redirect('admin_manage_department')
    else:
        messages.success(request, 'Some Thing is wrong!')
        return redirect('admin_manage_department')

#-------------------------------admin thesis project manage--------------------------------------
#------------------------- create thesis project manage -------------------
@login_required(login_url='admin_login')
def create_admin_thesis_project(request):
    departments = models.Department.objects.all().order_by('-id')
    project_type = models.Project_type.objects.all().order_by('-id')
    thesis_type = models.Thesis_type.objects.all().order_by('-id')
    context = {
              'department': departments,
              'project_type': project_type,
              'thesis_type': thesis_type,
         }
    if request.method == 'POST':
        thesis_project = models.Thesis_project_manage()
        thesis_project.user_id = request.user.id
        thesis_project.name = request.POST.get('name')
        thesis_project.type = request.POST.get('type')
        thesis_project.thesis_type_id = request.POST.get('thesis_type')
        thesis_project.project_type_id = request.POST.get('project_type')
        thesis_project.topic_name = request.POST.get('topic_name')
        thesis_project.supervisor_name = request.POST.get('supervisor_name')
        thesis_project.student_id = request.POST.get('student_id')
        thesis_project.teacher_id = request.POST.get('teacher_id')
        thesis_project.department_id = request.POST.get('department')
        thesis_project.batch = request.POST.get('batch')
        thesis_project.phone = request.POST.get('phone')
        thesis_project.email = request.POST.get('email')
        thesis_project.submit_by = request.POST.get('submit_by')
        thesis_project.description = request.POST.get('description')
        thesis_project.pdf = request.FILES.get('pdf')
        save = thesis_project.save()
        if not save:
            messages.success(request,'This Topic Create Successfully!')
            return redirect('create_admin_thesis_project')
        else:
            messages.warning(request, 'Something is Wrong!')
            return redirect('create_admin_thesis_project')

    return render(request,'views/auth/dashboard/thesis_project_manage/create_thesis_project.html',context)

#----------------------------- manage thesis project -----------------------
@login_required(login_url='admin_login')
def manage_admin_thesis_project(request):
    thesis_project = models.Thesis_project_manage.objects.all().order_by('-id')
    context = {
        'thesis_project': thesis_project,
    }
    return render(request,'views/auth/dashboard/thesis_project_manage/manage_thesis_project.html',context)
#----------------------------show pdf -----------------------------------
@login_required(login_url='admin_login')
def pdf_show_admin(request,id):
    show_pdf= models.Thesis_project_manage.objects.get(id=id)
    context={
        'show_pdf': show_pdf
    }
    return render(request, 'views/auth/dashboard/thesis_project_manage/show_pdf.html',context)

#------------------------- status thesis project ----------------------------
@login_required(login_url='admin_login')
def admin_thesis_project_status(request,id):
    data = models.Thesis_project_manage.objects.get(id=id)
    if data.status == True:
        models.Thesis_project_manage.objects.filter(id=id).update(status=False)
        messages.success(request,'Status Not Approved Successfully!')
        return redirect('manage_admin_thesis_project')
    elif data.status == False:
        models.Thesis_project_manage.objects.filter(id=id).update(status=True)
        messages.success(request,'Status Approved Successfully!')
        return redirect('manage_admin_thesis_project')

#-----------------------thesis project delete ---------------------
@login_required(login_url='admin_login')
def admin_thesis_project_delete(request,id):
    data = models.Thesis_project_manage.objects.get(id=id)
    if data:
        if data.pdf:
            if len(data.pdf) > 0:
                os.remove(data.pdf.path)
        data.delete()
        messages.success(request,'This Topic Delete Successfully!')
        return redirect('manage_admin_thesis_project')
    else:
        messages.warning(request,'Something is Wrong!')
        return redirect('manage_admin_thesis_project')

#-----------------------thesis project Update ----------------------
@login_required(login_url='admin_login')
def admin_thesis_project_update(request,id):
    thesis_project = models.Thesis_project_manage.objects.get(id=id)
    departments = models.Department.objects.all().order_by('-id')
    project_type = models.Project_type.objects.all().order_by('-id')
    thesis_type = models.Thesis_type.objects.all().order_by('-id')
    if request.method == 'POST':
        thesis_project.user_id = request.POST.get('user')
        thesis_project.name = request.POST.get('name')
        thesis_project.type = request.POST.get('type')
        thesis_project.thesis_type_id = request.POST.get('thesis_type')
        thesis_project.project_type_id = request.POST.get('project_type')
        thesis_project.topic_name = request.POST.get('topic_name')
        thesis_project.supervisor_name = request.POST.get('supervisor_name')
        thesis_project.student_id = request.POST.get('student_id')
        thesis_project.teacher_id = request.POST.get('teacher_id')
        thesis_project.department_id = request.POST.get('department')
        thesis_project.batch = request.POST.get('batch')
        thesis_project.phone = request.POST.get('phone')
        thesis_project.email = request.POST.get('email')
        thesis_project.submit_by = request.POST.get('submit_by')
        thesis_project.description = request.POST.get('description')
        pdf_cheack = request.FILES.get('pdf')
        if pdf_cheack:
            if  thesis_project.pdf:
                if len(thesis_project.pdf) > 0:
                    os.remove(thesis_project.pdf.path)
            thesis_project.pdf = pdf_cheack
        else:
            thesis_project.pdf = thesis_project.pdf
        save = thesis_project.save()
        if not save:
            messages.success(request, 'This Topic Update Successfully!')
            return redirect('manage_admin_thesis_project')
        else:
            messages.warning(request, 'Something is Wrong!')
            return redirect('manage_admin_thesis_project')
    context = {
        'data': thesis_project,
        'department': departments,
        'project_type': project_type,
        'thesis_type': thesis_type,
    }
    return render(request, 'views/auth/dashboard/thesis_project_manage/update_thesis_project.html', context)

#------------------------------Student thesis project manage--------------------------------------


#------------------------- create thesis project manage -------------------
@login_required(login_url='student_login')
def create_student_thesis_project(request):
    departments = models.Department.objects.all().order_by('-id')
    project_type = models.Project_type.objects.all().order_by('-id')
    thesis_type = models.Thesis_type.objects.all().order_by('-id')
    context = {
        'department': departments,
        'project_type': project_type,
        'thesis_type': thesis_type,
    }
    if request.method == 'POST':
        thesis_project = models.Thesis_project_manage()
        thesis_project.user_id = request.user.id
        thesis_project.name = request.POST.get('name')
        thesis_project.type = request.POST.get('type')
        thesis_project.thesis_type_id = request.POST.get('thesis_type')
        thesis_project.project_type_id = request.POST.get('project_type')
        thesis_project.topic_name = request.POST.get('topic_name')
        thesis_project.supervisor_name = request.POST.get('supervisor_name')
        thesis_project.student_id = request.POST.get('student_id')
        thesis_project.department_id = request.POST.get('department')
        thesis_project.batch = request.POST.get('batch')
        thesis_project.phone = request.POST.get('phone')
        thesis_project.email = request.POST.get('email')
        thesis_project.submit_by = 'student'
        thesis_project.description = request.POST.get('description')
        thesis_project.pdf = request.FILES.get('pdf')
        save = thesis_project.save()
        if not save:
            messages.success(request,'This Topic Create Successfully!')
            return redirect('create_student_thesis_project')
        else:
            messages.warning(request, 'Something is Wrong!')
            return redirect('create_student_thesis_project')

    return render(request,'views/student/dashboard/thesis_project_manage/create_thesis_project.html',context)

#----------------------------- manage thesis project -----------------------
@login_required(login_url='student_login')
def manage_student_thesis_project(request):
    find_current_id = request.user.id
    thesis_project = models.Thesis_project_manage.objects.filter(user_id=find_current_id).order_by('-id')
    context = {
        'thesis_project': thesis_project,
    }
    return render(request,'views/student/dashboard/thesis_project_manage/manage_thesis_project.html',context)

#----------------------------show pdf -----------------------------------
@login_required(login_url='student_login')
def pdf_show_student(request,id):
    show_pdf= models.Thesis_project_manage.objects.get(id=id)
    context={
        'show_pdf': show_pdf
    }
    return render(request, 'views/student/dashboard/thesis_project_manage/show_pdf.html',context)


#-------------------------------Teacher thesis project manage--------------------------------------


#------------------------- create thesis project -------------------
@login_required(login_url='teacher_login')
def create_teacher_thesis_project(request):
    departments = models.Department.objects.all().order_by('-id')
    project_type = models.Project_type.objects.all().order_by('-id')
    thesis_type = models.Thesis_type.objects.all().order_by('-id')
    context = {
              'department': departments,
              'project_type': project_type,
              'thesis_type': thesis_type,
         }
    if request.method == 'POST':
        thesis_project = models.Thesis_project_manage()
        thesis_project.user_id = request.user.id
        thesis_project.name = request.POST.get('name')
        thesis_project.thesis_type_id = request.POST.get('thesis_type')
        thesis_project.project_type_id = request.POST.get('project_type')
        thesis_project.type = request.POST.get('type')
        thesis_project.topic_name = request.POST.get('topic_name')
        thesis_project.supervisor_name = request.POST.get('supervisor_name')
        thesis_project.teacher_id = request.POST.get('teacher_id')
        thesis_project.department_id = request.POST.get('department')
        thesis_project.phone = request.POST.get('phone')
        thesis_project.email = request.POST.get('email')
        thesis_project.submit_by = 'teacher'
        thesis_project.description = request.POST.get('description')
        thesis_project.pdf = request.FILES.get('pdf')
        save = thesis_project.save()
        if not save:
            messages.success(request,'This Topic Create Successfully!')
            return redirect('create_teacher_thesis_project')
        else:
            messages.warning(request, 'Something is Wrong!')
            return redirect('create_teacher_thesis_project')

    return render(request,'views/teacher/dashboard/thesis_project/create_thesis_project.html',context)

#----------------------------- manage thesis project -----------------------
@login_required(login_url='teacher_login')
def manage_teacher_thesis_project(request):
    find_current_id = request.user.id
    thesis_project = models.Thesis_project_manage.objects.filter(user_id=find_current_id ) | models.Thesis_project_manage.objects.filter(submit_by= 'student' )
    context = {
        'thesis_project': thesis_project,
    }
    return render(request,'views/teacher/dashboard/thesis_project/manage_thesis_project.html',context)

#----------------------------show pdf -----------------------------------
@login_required(login_url='teacher_login')
def pdf_show_teacher(request,id):
    show_pdf= models.Thesis_project_manage.objects.get(id=id)
    context={
        'show_pdf': show_pdf
    }
    return render(request, 'views/teacher/dashboard/thesis_project/show_pdf.html',context)

#------------------------- status thesis project ----------------------------
@login_required(login_url='teacher_login')
def teacher_thesis_project_status(request,id):
    data = models.Thesis_project_manage.objects.get(id=id)
    if data.status == True:
        models.Thesis_project_manage.objects.filter(id=id).update(status=False)
        messages.success(request,'Status  Not Approved Successfully!')
        return redirect('manage_teacher_thesis_project')
    elif data.status == False:
        models.Thesis_project_manage.objects.filter(id=id).update(status=True)
        messages.success(request,'Status Approved Successfully!')
        return redirect('manage_teacher_thesis_project')

#-----------------------thesis project Update ----------------------
@login_required(login_url='teacher_login')
def teacher_thesis_project_update(request,id):
    thesis_project = models.Thesis_project_manage.objects.get(id=id)
    departments = models.Department.objects.all().order_by('-id')
    project_type = models.Project_type.objects.all().order_by('-id')
    thesis_type = models.Thesis_type.objects.all().order_by('-id')
    if request.method == 'POST':
        thesis_project.name = request.POST.get('name')
        thesis_project.type = request.POST.get('type')
        thesis_project.thesis_type_id = request.POST.get('thesis_type')
        thesis_project.project_type_id = request.POST.get('project_type')
        thesis_project.topic_name = request.POST.get('topic_name')
        thesis_project.supervisor_name = request.POST.get('supervisor_name')
        thesis_project.student_id = request.POST.get('student_id')
        thesis_project.teacher_id = request.POST.get('teacher_id')
        thesis_project.department_id = request.POST.get('department')
        thesis_project.batch = request.POST.get('batch')
        thesis_project.phone = request.POST.get('phone')
        thesis_project.email = request.POST.get('email')
        thesis_project.submit_by = request.POST.get('submit_by')
        thesis_project.description = request.POST.get('description')
        pdf_cheack = request.FILES.get('pdf')
        if pdf_cheack:
            if  thesis_project.pdf:
                if len(thesis_project.pdf) > 0:
                    os.remove(thesis_project.pdf.path)
            thesis_project.pdf = pdf_cheack
        else:
            thesis_project.pdf = thesis_project.pdf
        save = thesis_project.save()
        if not save:
            messages.success(request, 'This Topic Update Successfully!')
            return redirect('manage_teacher_thesis_project')
        else:
            messages.warning(request, 'Something is Wrong!')
            return redirect('manage_teacher_thesis_project')
    context = {
        'data': thesis_project,
        'department': departments,
        'project_type': project_type,
        'thesis_type': thesis_type,
    }
    return render(request, 'views/teacher/dashboard/thesis_project/update_thesis_project.html', context)

#-----------------------thesis project delete ---------------------
@login_required(login_url='teacher_login')
def teacher_thesis_project_delete(request,id):
    data = models.Thesis_project_manage.objects.get(id=id)
    if data:
        if data.pdf:
            if len(data.pdf) > 0:
                os.remove(data.pdf.path)
        data.delete()
        messages.success(request,'This Topic Delete Successfully!')
        return redirect('manage_teacher_thesis_project')
    else:
        messages.warning(request,'Something is Wrong!')
        return redirect('manage_teacher_thesis_project')