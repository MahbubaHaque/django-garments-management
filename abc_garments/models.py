from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Employee(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    salary=models.IntegerField()
    birth_date=models.DateField()
    phone=models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

class Product(models.Model):
    name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
    size=models.CharField(max_length=10) #XL,M,S
    price=models.IntegerField()

    def __str__(self):
        return self.name


class Delivery(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    shipment_id=models.CharField(max_length=20,blank=True)
    delivery_owner=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_bill=models.IntegerField(default=0)
    delivery_date=models.DateField()
    
    def __str__(self):
        return "Owner {}".format(self.delivery_owner.username)


class MadeProduct(models.Model):
    emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} made {} products".format(emp_id.name,quantity)
