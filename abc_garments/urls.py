from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from .views import products
urlpatterns=[
    path('products/',products,name='products'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)