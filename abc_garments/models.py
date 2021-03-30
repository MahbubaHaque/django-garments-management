from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image
from django.core.files import File

def compress(image):
    im = Image.open(image)
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=60) 
    new_image = File(im_io, name=image.name)
    return new_image
    

class Employee(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    salary=models.IntegerField()
    birth_date=models.DateField()
    phone=models.CharField(max_length=20)
    supervisor=models.IntegerField(default=0)
    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

class Product(models.Model):
    name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
    size=models.CharField(max_length=10) #XL,M,S
    price=models.IntegerField()
    image=models.ImageField(upload_to='products',blank=True,null=True)

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super(Product,self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    shipment_id=models.CharField(max_length=20,blank=True)
    delivery_owner=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_bill=models.IntegerField(default=0)
    
    def __str__(self):
        return "Owner {}".format(self.delivery_owner.username)


class MadeProduct(models.Model):
    emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} made {} products".format(self.emp_id.name,self.quantity)


class Materials(models.Model):
    name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MaterialsUsed(models.Model):
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    materials_id=models.ForeignKey(Materials,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} used {} {}".format(self.employee_id.name,self.quantity,self.materials_id.name)


class Attendance(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    delivery_date=models.DateField()

    def __str__(self):
        return self.employee.name


class PartTimeWork(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    worked_hour=models.IntegerField()
    worked_date=models.DateField()

    def __str__(self):
        return self.employee.name


class Query(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=70)
    message=models.TextField()

    def __str__(self):
        return "query from {} {}".format(self.first_name,self.last_name)