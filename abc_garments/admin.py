from django.contrib import admin

from .models import Product,Delivery,Employee,MadeProduct,Materials,MaterialsUsed,Attendance,PartTimeWork
# Register your models here.
admin.site.site_header = "ABC garments"


admin.site.register(Product)
admin.site.register(Delivery)
admin.site.register(Employee)
admin.site.register(MadeProduct)
admin.site.register(Materials)
admin.site.register(MaterialsUsed)
admin.site.register(Attendance)
admin.site.register(PartTimeWork)
