from django.contrib import admin

from .models import Product,Delivery,Employee,MadeProduct
# Register your models here.
admin.site.site_header = "ABC garments"


admin.site.register(Product)
admin.site.register(Delivery)
admin.site.register(Employee)
admin.site.register(MadeProduct)
