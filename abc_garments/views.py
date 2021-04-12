from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .models import Product,Delivery,Query,Employee,Attendance,Notification, Materials, MaterialsUsed
from .forms import EmployeeForm,NotificationForm, MaterialsForm, MaterialsUsedForm
import string
import random

@login_required
def products(request):
    context={}
    products=Product.objects.all()
    context['products']=products
    return render(request,'products.html',context)


@login_required
def buyProduct(request,id=None):
    context={}
    product=Product.objects.get(pk=id)
    context['product']=product

    if request.method=="POST":
        quantity=request.POST['quantity']
        total_bill=int(quantity)*product.price
        #print(total_bill)
        shipment_id= ''.join(random.choices(string.ascii_uppercase +string.digits, k = 10))
        Delivery.objects.create(product=product,quantity=quantity,shipment_id=shipment_id,delivery_owner=request.user,total_bill=total_bill)
        messages.success(request,"Order recieved successfully Thank You for being with us")
        return redirect('home')
    else:
        #print(product)
        return render(request,'buy_product.html',context)


def about(request):

    if request.method=="POST":
        #print(request.POST)
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        message=request.POST['message']
        Query.objects.create(first_name=first_name,last_name=last_name,email=email,message=message)
        messages.success(request,"Your message recieved You will be replied soon . Thank You")
        return redirect('home')
    else:
        return render(request,'about_us.html')

@login_required
def allOrders(request):
    context={}
    if request.method=="POST":
        from_date=request.POST["from"]
        to_date=request.POST["to"]
        orders=Delivery.objects.filter(created_at__range=(from_date, to_date))
        context['orders']=orders
    else:

        orders=Delivery.objects.all()
        context['orders']=orders
    return render(request,'admin/all_orders.html',context)

@login_required
def deleteOrder(request,id=None):
    order=Delivery.objects.get(pk=id)
    order.delete()
    messages.warning(request,"This Order deleted successfully")
    return redirect('all_orders')

@login_required
def addEmployee(request):

    context={}
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            #print("form is valid")
            employee=form.save(commit=False)
            employee.save()
            messages.success(request,"Employee Saved Successfully")
        return redirect('profile',id=request.user.id)
    else:
        form=EmployeeForm()
        context['form']=form
    return render(request,'admin/add_employee.html',context)

@login_required
def deleteEmployee(request,id=None):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    messages.warning(request,"Employee deleted successfully")
    return redirect('all_employee')

def allEmployee(request):
    context={}
    employees=Employee.objects.all()
    context['employees']=employees
    return render(request,'admin/all_employee.html',context)

@login_required
def takeAttendence(request):
    context={}
    employees=Employee.objects.all()
    context['employees']=employees
    if request.method=="POST":
        attendence_date=request.POST["attendence_date"]
        
        attend=Attendance.objects.filter(attendence_date=attendence_date)
        if len(attend):
            messages.success(request,"Attendance already taken in this date")
            return redirect('take_attendence')   

        for i in range(len(employees)):
            present=request.POST["is_present-{}".format(employees[i].id)]
            Attendance.objects.create(employee=employees[i],is_present=bool(present),attendence_date=attendence_date)

        messages.success(request,"Attendence of date {} taken Successfully".format(attendence_date))
        return redirect('profile',id=request.user.id)
    else:
        return render(request,'admin/take_attendence.html',context)

@login_required
def notification(request):

    context={}

    if request.method=="POST":
        form=NotificationForm(request.POST)
        if form.is_valid():
            #print("form is valid")
            notification=form.save(commit=False)
            notification.save()
            messages.success(request,"Notification Sent Successfully")
        return redirect('profile',id=request.user.id)
    else:
        form=NotificationForm()
        context['form']=form
        return render(request,'admin/notification.html',context)
        
@login_required
def deleteNotification(request,id=None):
    notification=Notification.objects.get(pk=id)
    notification.delete()
    messages.success(request,"Your One notification deleted")
    return redirect('profile',id=request.user.id)



@login_required
def add_materials(request):
    
    if request.method == "POST":
        forms = MaterialsForm(request.POST)
        if forms.is_valid:
            forms.save()
    forms = MaterialsForm()
    context = {
        "form" : forms
    }
    return render(request,"admin/add_materials.html",context)

@login_required
def show_materials(request):
    materials = Materials.objects.all()
    print(len(materials))
    context={
        "materials" : materials
    }
    return render(request,"admin/show_materials.html", context)



@login_required
def add_materialsused(request):
    
    if request.method == "POST":
        forms = MaterialsUsedForm(request.POST)
        if forms.is_valid:
            forms.save()
    forms = MaterialsUsedForm()
    context = {
        "form" : forms
    }
    return render(request,"admin/add_materials_used.html",context)

@login_required
def show_materialsused(request):
    materialsused = MaterialsUsed.objects.all()
    
    context={
        "materials" : materialsused
    }
    return render(request,"admin/show_materials_used.html", context)


@login_required
def toggleDeliveryStatus(request,id=None):
    order=Delivery.objects.get(pk=id)
    order.is_delivered=(False if order.is_delivered else True)
    order.save()
    messages.warning(request,"This Order delivery status changed successfully")
    return redirect('all_orders')