from django.urls import path
from .views import (signup,logout,loginView,
    userProfile,updateUserProfile)
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns=[
    path('signup/',signup,name='signup'),
    path('logout/',logout,name='logout'),
    path('login/',loginView,name='login'),
    path('profile/<int:id>/',userProfile,name='profile'),
    path('update_user_profile/<int:id>/',updateUserProfile,name='update_user_profile'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)