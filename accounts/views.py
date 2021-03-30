from django.shortcuts import render,redirect
from .forms import SignUpForm,UserLoginForm
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UpdateUserProfileForm


def loginView(request):
    context={}

    if request.method=="POST":
        form=UserLoginForm(request.POST)

        if form.is_valid():
            user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])

            if user:
                auth.login(request,user)
                messages.success(request,"You Loggedin Successfully")
                return redirect('home')
            else:
                messages.error(request,"Please Provide Correct Data")
                return redirect('login')
        
        else:
            messages.error(request,"Some Error in login Form")
            return redirect('login')

    else:
        form=UserLoginForm()
        context['form']=form
    
    return render(request,'authentication/login.html',context)

    

def signup(request):

    context={}

    if request.method=="POST":
        form=SignUpForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            user = auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password1'))
            
            if user:
                auth.login(request,user)
            messages.success(request,"User Saved Successfully")
            UserProfile.objects.create(customer=user)
            return redirect('home')
        else:
            messages.error(request,"Error In this form")
            return redirect('signup')
    else:
        form=SignUpForm()
        context['form']=form
        #print(context)


    return render(request,'authentication/signup.html',context)

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')

@login_required
def userProfile(request,id=None):
    user=User.objects.get(pk=id)
    
    context={}
    if user.is_superuser:
        return render(request,'admin/base_admin.html',context)
    else:
        profile=UserProfile.objects.get(customer=user)
        context['id']=id
        context['profile']=profile
        return render(request,'authentication/user_profile.html',context)

@login_required
def updateUserProfile(request,id=None):

    context={}
    if request.method=="POST":
        user=User.objects.get(pk=id)
        user_profile=UserProfile.objects.get(customer=user)
        form=UpdateUserProfileForm(request.POST,request.FILES,instance=user_profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,  'Your Profile Updated Successfully')
            return redirect('profile',id)
        else:
            messages.add_message(request, messages.ERROR,  'Update data is not valid')
            return redirect('profile',id=id)
    else:
        user=User.objects.get(pk=id)
        user_profile=UserProfile.objects.get(customer=user)
        form=UpdateUserProfileForm(instance=user_profile)
        context['form']=form
        #print(form)
        return render(request,'authentication/update_user_profile.html',context)