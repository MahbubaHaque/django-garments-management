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


class UserProfile(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='customer',blank=True,null=True)
    profession=models.CharField(max_length=100,blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    address=models.CharField(max_length=255,blank=True,null=True)
    facebook=models.URLField(max_length=255,blank=True,null=True)
    twitter=models.URLField(max_length=255,blank=True,null=True)
    phone=models.CharField(max_length=50,blank=True,null=True)
    fax=models.CharField(max_length=50,blank=True,null=True)

    def save(self, *args, **kwargs):
        if self.image:
            new_image = compress(self.image)
            self.image = new_image
        super(UserProfile,self).save(*args, **kwargs)

    def __str__(self):
        return "Profile of {}".format(self.customer.username)
