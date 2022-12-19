from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
import os
from django.contrib.auth import authenticate,logout,login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from auth_dashboard_App.models import User
from thesis_project_manage_App.models import Thesis_project_manage
from .import models,forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
#------------- auth registration ---------------#
@login_required(login_url='admin_login')
def auth_reg(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        con_password = request.POST.get('confirm-password')
        cheack_username = request.POST.get('username')
        if password == con_password:
            if models.User.objects.filter(username=cheack_username):
                user_name_error = 'This UserName Already Exist'
                return render(request, 'views/auth/authentication/auth_registration.html',{'user_name_error':user_name_error})
            else:
                users = models.User()
                users.username = request.POST.get('username')
                users.email = request.POST.get('email')
                users.is_superuser = True
                users.is_staff = True
                users.set_password(password)
                users.save()
                messages.success(request, 'Registration Successfully!')
        else:
            messages.warning(request, "Password and confirm-password don't match")
    return render(request, 'views/auth/authentication/auth_registration.html')
#-------------------------- auth login ------------------------
def auth_login(request):
    if request.user.is_superuser == True:
        return redirect('admin_home')
    if request.method == 'POST':
        password = request.POST.get('password')
        cheack_username = request.POST.get('username')
        user = authenticate(username=cheack_username, password=password)
        if user:
            user_info =models.User.objects.get(id=user.id)
            # request.session['username'] = user_info.username
            # request.session['is_superuser'] = user_info.is_superuser
            # request.session['user_id'] = user_info.id
            if user_info.is_superuser == True  and  user_info.is_staff == True:
                login(request, user)
                return redirect('admin_reg')
            else:
                messages.warning(request, 'you are not registered admin')
        else:
            messages.warning(request, 'Your username or password is invalid.')

    return render(request, 'views/auth/authentication/auth_login.html')

#-------------------------auth logout -----------------------#
@login_required(login_url='admin_login')
def auth_logout(request):
    logout(request)
    return redirect('home')
#---------------------------- user manage --------------------#
@login_required(login_url='admin_login')
def user_manage(request):
    user = User.objects.all().order_by('-id')
    context ={
        'users':user,
    }
    return render(request,'views/auth/authentication/manage_user.html',context)

#------------------------- user status ----------------------------
@login_required(login_url='admin_login')
def user_status(request,id):
    data = User.objects.get(id=id)
    user_name = data.username
    if data.is_active == 1:
        User.objects.filter(id=id).update(is_active=0)
        messages.success(request,user_name +' '+'Status Deactive Successfully!')
        return redirect('user_manage')
    elif data.is_active == 0:
        User.objects.filter(id=id).update(is_active=1)
        messages.success(request,user_name + ' ' + 'Status Active Successfully!')
        return redirect('user_manage')

#------------------------------ user delete------------------------
@login_required(login_url='admin_login')
def user_delete(request,id):
    data = User.objects.get(id=id)
    user_name = data.username
    if data:
        data.delete()
        messages.success(request,'User'+' '+user_name+' '+' Delete Successfully!')
        return redirect('user_manage')
    else:
        messages.warning(request,'Something is Wrong!')
        return redirect('user_manage')

#--------------------------------- Create profile ---------------------------
@login_required(login_url='admin_login')
def create_admin_profile(request):
    user_name = User.objects.filter(is_superuser='1').order_by('-id')
    if request.method == 'POST':
        cheack_username = request.POST.get('user')
        user_name_info = User.objects.get(id=cheack_username)
        if models.auth_profile_customer.objects.filter(user_id=cheack_username):
                messages.warning(request, 'This UserName Already Exist')
        else:
            user_pro = models.auth_profile_customer()
            user_pro.user_id = cheack_username
            user_pro.address = request.POST.get('address')
            user_pro.phone = request.POST.get('phone')
            user_pro.about = request.POST.get('about')
            user_pro.image = request.FILES.get('image')
            user_name_info.first_name = request.POST.get('first_name')
            user_name_info.last_name = request.POST.get('last_name')
            save_user = user_name_info.save()
            save = user_pro.save()
            if not save:
                messages.success(request,'User name' + ' ' + user_name_info.username+ ' ' + ' information Create Successfully!')
                return redirect('create_admin_profile')
            else:
                messages.warning(request, 'Something is Wrong!')
                return redirect('create_admin_profile')
    context ={
        'user_name':user_name,
    }
    return render(request,'views/auth/dashboard/admin_profile/create_admin_profile.html',context)
#--------------------------------- manage profile-------------------
@login_required(login_url='admin_login')
def manage_admin_profile(request):
    admin_info = models.auth_profile_customer.objects.all().order_by('-id')
    context ={
        'admin_info':admin_info,
    }
    return render(request,'views/auth/dashboard/admin_profile/manage_admin_profile.html',context)

#-----------------------Admin Profile delete -----------------
@login_required(login_url='admin_login')
def admin_profile_delete(request,id):
    data = models.auth_profile_customer.objects.get(id=id)
    if data:
        if data.image:
            if len(data.image) > 0:
                os.remove(data.image.path)
        user_name = data.user.username
        data.delete()
        messages.success(request,'User name'+' '+user_name+' '+'Information Delete Successfully!')
        return redirect('manage_admin_profile')
    else:
        messages.warning(request,'Something is Wrong!')
        return redirect('manage_admin_profile')

#-------------------------- Admin Profile Update --------------------------
@login_required(login_url='admin_login')
def update_admin_profile(request,id):
    admin_pro = models.auth_profile_customer.objects.get(id=id)
    user_name = admin_pro.username
    if request.method == 'POST':
        user_info = models.User.objects.get(id=admin_pro.id)
        user_info.email = request.POST.get('email')
        user_info.first_name = request.POST.get('first_name')
        user_info.last_name = request.POST.get('last_name')

        admin_pro.about = request.POST.get('about')
        admin_pro.phone = request.POST.get('phone')
        admin_pro.address = request.POST.get('address')
        image_cheack = request.FILES.get('image')
        if image_cheack:
            if admin_pro.image:
                if len(admin_pro.image) > 0:
                    os.remove(admin_pro.image.path)
            admin_pro.image = image_cheack
        else:
            admin_pro.image = admin_pro.image
        save_user = user_info.save()
        save = admin_pro.save()
        if not save:
            messages.success(request, 'User name' + ' ' + user_name + ' ' + 'Information Update Successfully!')
            return redirect('manage_admin_profile')
        else:
            messages.warning(request, 'Something is Wrong!')
            return redirect('manage_admin_profile')
    context = {
        'admin_pro': admin_pro
    }
    return render(request,'views/auth/dashboard/admin_profile/update_admin_profile.html',context)

#------------------------- show admin profile ----------------------
@login_required(login_url='admin_login')
def show_admin_profile(request):
    user_id = request.user.id
    user_info = models.User.objects.get(id=user_id)
    context ={
        'user_info':user_info,
    }
    return render(request, 'views/auth/dashboard/admin_profile/show_admin_profile.html',context)
#------------ home page ---------------
@login_required(login_url='admin_login')
def home(request):
    count_user = models.User.objects.count()
    count_thesis = Thesis_project_manage.objects.filter(type ='thesis').count()
    count_project = Thesis_project_manage.objects.filter(type='project').count()
    context ={
        'count_user': count_user,
        'count_thesis':count_thesis,
        'count_project':count_project,
    }
    return render(request, 'views/auth/dashboard/home.html',context)


#------------ manage contact page ---------------
@login_required(login_url='admin_login')
def manage_contact (request):
    contact = models.Contact.objects.all().order_by('-id')
    context ={
        'contact': contact,
    }
    return render(request, 'views/auth/dashboard/contact/manage_contact.html',context)

#------------ Delete contact  ---------------
@login_required(login_url='admin_login')
def delete_contact (request,id):
    data = models.Contact.objects.get(id=id)
    if data:
        data.delete()
        messages.success(request, 'Contact Delete Successfully!')
        return redirect('manage_contact')
    else:
        messages.warning(request, 'Something is Wrong!')
        return redirect('manage_contact')

#------------ Update contact  ---------------
@login_required(login_url='admin_login')
def update_contact (request,id):
    contact = models.Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message')
        contact.save()
        messages.success(request, 'Update Message Successfully!')
        return redirect('manage_contact')
    else:
        messages.warning(request, "Message Not  Send ")
    context = {
        'contact': contact,
    }
    return render(request, 'views/auth/dashboard/contact/update_contact.html', context)