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

# Create your views here.
#------------------ student registration -----------------#
def student_reg(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        con_password = request.POST.get('confirm-password')
        cheack_username = request.POST.get('username')
        cheack_student_id = request.POST.get('student_id')
        if User.objects.filter(student_id=cheack_student_id):
            user_stu_id_error = 'This Student Id Already Exist'
            return render(request,'views/student/account/student_registration.html',
                          {'user_stu_id_error': user_stu_id_error})
        else:
            if password == con_password:
                if User.objects.filter(username=cheack_username):
                    user_name_error = 'This UserName Already Exist'
                    return render(request, 'views/student/account/student_registration.html',{'user_name_error':user_name_error})
                else:
                    user = User()
                    user.username = request.POST.get('username')
                    user.email = request.POST.get('email')
                    user.set_password(password)
                    user.is_student = True
                    user.student_id = request.POST.get('student_id')
                    user.save()
                    current_site = get_current_site(request)
                    mail_subject = 'An registration successfully'
                    message = render_to_string('views/student/email/reg_successfully_email.html', {
                            'user': request.POST.get('username'),
                            'domain': current_site.domain
                        })
                    send_mail = request.POST.get('email')
                    email = EmailMessage(mail_subject, message, to=[send_mail])
                    email.send()
                    messages.success(request,'Registration Successfully!')
            else:
                messages.warning(request, "Password and confirm-password don't match")
    return render(request,'views/student/account/student_registration.html')

#---------------------------- student login -------------------#
def student_login(request):
    if request.user.is_authenticated:
       if request.user.is_student == True:
        return redirect('stu_profile_show')
    if request.method == 'POST':
        password = request.POST.get('password')
        cheack_username = request.POST.get('username')
        cheack_student_id = request.POST.get('student_id')
        user = authenticate(username=cheack_username, password=password)
        if user:
            user_info = User.objects.get(id = user.id)
            # request.session['username'] = user_info.username
            # request.session['is_student'] = user_info.is_student
            # request.session['user_id'] = user_info.id
            if user_info.is_student == True:
                if  user_info.student_id == cheack_student_id :
                    login(request, user)
                    return redirect('stu_profile_show')
                else:
                    user_stu_id_error = 'This student id not matching'
                    return render(request,'views/student/account/student_login.html',
                                  {'user_stu_id_error': user_stu_id_error})
            else:
                messages.warning(request, 'you are not registered student')
        else:
             messages.warning(request, 'Your username or password is invalid.')
    return render (request,'views/student/account/student_login.html')
#-------------------------student logout -----------------------#
def student_logout(request):
    logout(request)
    return redirect('home')

#---------------------------- home page ---------------------------#
@login_required(login_url='student_login')
def home(request):
    return render(request,'views/student/dashboard/home.html')


#---------------- show student profile ------------------#
def stu_profile_show(request):
    find_current_id = request.user.id
    user_info = User.objects.get(id=find_current_id)
    thesis_project = Thesis_project_manage.objects.filter(user_id=find_current_id).order_by('-id')
    count_thesis = Thesis_project_manage.objects.filter(user_id=find_current_id,type='thesis').count()
    count_project = Thesis_project_manage.objects.filter(user_id=find_current_id,type='project').count()
    context ={
           'stu_profile':user_info,
           'thesis_project': thesis_project,
           'count_thesis':count_thesis,
           'count_project':count_project,
       }
    return render(request, 'views/student/profile/show_student_profile.html',context)

#---------------- edit student profile ------------------#
@login_required(login_url='student_login')
def stu_profile_update(request,id):
    user_info = User.objects.get(id=id)
    if request.method == 'POST':
        user_info.username = request.POST.get('username')
        user_info.email = request.POST.get('email')
        user_info.first_name = request.POST.get('first_name')
        user_info.last_name = request.POST.get('last_name')
        user_info.student_id = request.POST.get('student_id')
        stu_profile = models.Student_profile()
        stu_profile.user_id = user_info.id
        stu_profile.department = request.POST.get('department')
        stu_profile.about = request.POST.get('about')
        stu_profile.phone = request.POST.get('phone')
        stu_profile.address = request.POST.get('address')
        stu_profile.batch = request.POST.get('batch')
        image_new = request.FILES.get('image')
        if image_new:
            stu_profile.image = image_new
        else:
             stu_profile.image = request.POST.get('old_image')
        if not stu_profile.save() and not user_info.save():
            messages.success(request, 'User name' + ' ' + user_info.username + ' ' + ' information Update Successfully!')
            return redirect('manage_student')
        else:
            messages.warning(request, 'Something is Wrong!')
            return redirect('manage_student')
    context = {
        'user_info': user_info,
    }

    return render(request, 'views/student/profile/edit_student_profile.html',context)


#---------------------------- manage student page ---------------------------#
@login_required(login_url='student_login')
def manage_student(request):
    find_current_id = request.user.id
    user_info = User.objects.get(id=find_current_id)
    context = {
        'user_info' : user_info
    }
    return render(request, 'views/student/profile/manage_student_profile.html',context)

#----------------------- delete student information ---------------------
@login_required(login_url='student_login')
def stu_info_delete(request,id):
    data = models.Student_profile.objects.get(user_id=id)
    user_name = data.user.username
    if data:
        data.delete()
        messages.success(request,'User'+' '+user_name+' '+'Information Delete Successfully!')
        return redirect('manage_student')
    else:
        messages.warning(request,'Something is Wrong!')
        return redirect('manage_student')