from django.shortcuts import render,redirect
from .forms import SignUpForm,UserLoginForm
from django.contrib import messages,auth
# Create your views here.


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
