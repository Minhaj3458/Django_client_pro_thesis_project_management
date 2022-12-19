from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from auth_dashboard_App.models import User
from .import models , forms
import os
from django.contrib.auth import authenticate,logout,login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from thesis_project_manage_App.models import Thesis_project_manage

#------------------ teacher registration -----------------#
def teacher_reg(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        con_password = request.POST.get('confirm-password')
        cheack_username = request.POST.get('username')
        cheack_teacher_id = request.POST.get('teacher_id')
        if User.objects.filter(teacher_id=cheack_teacher_id):
            user_stu_id_error = 'This Teacher Id Already Exist'
            return render(request,'views/teacher/account/teacher_registration.html',
                          {'user_stu_id_error': user_stu_id_error})
        else:
            if password == con_password:
                if User.objects.filter(username=cheack_username):
                    user_name_error = 'This UserName Already Exist'
                    return render(request, 'views/teacher/account/teacher_registration.html',{'user_name_error':user_name_error})
                else:
                    user = User()
                    user.username = request.POST.get('username')
                    user.email = request.POST.get('email')
                    user.set_password(password)
                    user.is_teacher = True
                    user.teacher_id = request.POST.get('teacher_id')
                    user.save()
                    messages.success(request,'Registration Successfully!')
            else:
                messages.warning(request, "Password and confirm-password don't match")
    return render(request,'views/teacher/account/teacher_registration.html')

#--------------------------- teacher login -------------------#
def teacher_login(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teacher_profile')
    if request.method == 'POST':
        password = request.POST.get('password')
        cheack_username = request.POST.get('username')
        cheack_teacher_id = request.POST.get('teacher_id')
        user = authenticate(username=cheack_username, password=password)
        if user:
            user_info = User.objects.get(id = user.id)
            if user_info.is_teacher == True:
                if  user_info.teacher_id == cheack_teacher_id:
                    login(request, user)
                    return redirect('teacher_profile')
                else:
                    user_teach_id_error = 'This teacher id not matching'
                    return render(request,'views/teacher/account/teacher_login.html',
                                  {'user_teach_id_error': user_teach_id_error})
            else:
                messages.warning(request, 'you are not registered teacher')
        else:
             messages.warning(request, 'Your username or password is invalid.')
    return render (request,'views/teacher/account/teacher_login.html')

#------------------------------- teacher profile ------------------------
@login_required(login_url='teacher_login')
def teacher_profile(request):
    find_current_id = request.user.id
    user_info = User.objects.get(id=find_current_id)
    thesis_project = Thesis_project_manage.objects.filter(user_id=find_current_id).order_by('-id')[:5]
    count_thesis = Thesis_project_manage.objects.filter(user_id=find_current_id, type='thesis').count()
    count_project = Thesis_project_manage.objects.filter(user_id=find_current_id, type='project').count()
    context = {
        'teacher_profile': user_info,
        'thesis_project': thesis_project,
        'count_thesis': count_thesis,
        'count_project': count_project,
    }
    return render(request, 'views/teacher/profile/show_teacher_profile.html',context)
#-------------------------- teacher logout ----------------------#
@login_required(login_url='teacher_login')
def teacher_logout(request):
    logout(request)
    return redirect('home')
#---------------------------- update teacher profile --------------------------
@login_required(login_url='teacher_login')
def update_teacher_profile(request,id):
    user_info = User.objects.get(id=id)
    if request.method == 'POST':
        user_info.username = request.POST.get('username')
        user_info.email = request.POST.get('email')
        user_info.first_name = request.POST.get('first_name')
        user_info.last_name = request.POST.get('last_name')
        user_info.teacher_id = request.POST.get('teacher_id')
        teach_profile = models.Teacher_profile()
        teach_profile.user_id = user_info.id
        teach_profile.department = request.POST.get('department')
        teach_profile.about = request.POST.get('about')
        teach_profile.phone = request.POST.get('phone')
        teach_profile.address = request.POST.get('address')
        image_new = request.FILES.get('image')
        if image_new:
            teach_profile.image = image_new
        else:
            teach_profile.image = request.POST.get('old_image')
        if not teach_profile.save() and not user_info.save():
            messages.success(request,
                             'User name' + ' ' + user_info.username + ' ' + ' information Update Successfully!')
            return redirect('manage_teacher_profile')
        else:
            messages.warning(request, 'Something is Wrong!')
            return redirect('manage_teacher_profile')
    context = {
        'user_info':user_info
    }
    return render(request, 'views/teacher/profile/update_teacher_profile.html', context)

#--------------------------- manage teacher profile -----------------
@login_required(login_url='teacher_login')
def manage_teacher_profile(request):
    find_current_id = request.user.id
    user_info = User.objects.get(id=find_current_id)
    context = {
        'user_info': user_info
    }
    return render(request, 'views/teacher/profile/manage_teacher_profile.html',context)

#------------------------------- delete teacher profile -----------------
@login_required(login_url='teacher_login')
def delete_teacher_profile(request,id):
        data = models.Teacher_profile.objects.get(user_id=id)
        user_name = data.user.username
        if data:
            data.delete()
            messages.success(request, 'User' + ' ' + user_name + ' ' + 'Information Delete Successfully!')
            return redirect('manage_teacher_profile')
        else:
            messages.warning(request, 'Something is Wrong!')
            return redirect('manage_teacher_profile')

#------------------------------ teacher manage student ----------------------------
@login_required(login_url='teacher_login')
def teacher_manage_student(request):
    user = User.objects.filter(is_student = True).order_by('-id')
    context = {
        'users': user,
    }
    return render(request, 'views/teacher/dashboard/student_manage/manage_student.html',context)
#------------------------------ teacher manage student status ----------------------
@login_required(login_url='teacher_login')
def student_status(request,id):
    data = User.objects.get(id=id)
    user_name = data.username
    if data.is_active == 1:
        User.objects.filter(id=id).update(is_active=0)
        messages.success(request,user_name +' '+'Status Deactive Successfully!')
        return redirect('teacher_manage_student')
    elif data.is_active == 0:
        User.objects.filter(id=id).update(is_active=1)
        messages.success(request,user_name + ' ' + 'Status Active Successfully!')
        return redirect('teacher_manage_student')

#--------------------------------- teacher delete student -------------------------
@login_required(login_url='teacher_login')
def delete_student(request,id):
    data = User.objects.get(id=id)
    user_name = data.username
    if data:
        data.delete()
        messages.success(request, 'User' + ' ' + user_name + ' ' + ' Delete Successfully!')
        return redirect('teacher_manage_student')
    else:
        messages.warning(request, 'Something is Wrong!')
        return redirect('teacher_manage_student')