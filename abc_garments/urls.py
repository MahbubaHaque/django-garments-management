from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from .views import (products,buyProduct,about,allOrders,deleteOrder, add_materials, show_materials,add_materialsused, show_materialsused,
    allEmployee,addEmployee,deleteEmployee,takeAttendence,notification,deleteNotification,
    toggleDeliveryStatus)

urlpatterns=[
    path('products/',products,name='products'),
    path('buy_product/<int:id>/',buyProduct,name='buy_product'),
    path('about_us/',about,name='about'),
    path('all_orders',allOrders,name='all_orders'),
    path('delete_order/<int:id>/',deleteOrder,name='delete_order'),
    path('all_employee/',allEmployee,name='all_employee'),
    path('add_employee',addEmployee,name='add_employee'),
    path('delete_employee/<int:id>/',deleteEmployee,name='delete_employee'),
    path('take_attendence/',takeAttendence,name='take_attendence'),
    path('notification/',notification,name='notification'),
    path('delete_notification/<int:id>/',deleteNotification,name='delete_notification'),
    path('add_materials/',add_materials,name='add_materials'),
    path('show_materials/',show_materials,name='show_materials'),
    path('add_materials_used/',add_materialsused,name='add_materials_used'),
    path('show_materials_used/',show_materialsused,name='show_materials_used'),
    path('toggle_delivery_status/<int:id>/',toggleDeliveryStatus,name='toggle_delivery_status'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)