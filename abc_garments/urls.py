from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from .views import products,about,buyProduct,allOrders,deleteOrder,allEmployee

urlpatterns=[
    path('products/',products,name='products'),
    path('about_us/',about,name='about'),
    path('buy_product/<int:id>/',buyProduct,name='buy_product'),
    path('all_orders',allOrders,name='all_orders'),
    path('delete_order/<int:id>/',deleteOrder,name='delete_order'),
    path('all_employee/',allEmployee,name='all_employee'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)