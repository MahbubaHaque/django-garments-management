from django.urls import path
from .views import (signup,logout,loginView,
    userProfile,updateUserProfile)
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 

urlpatterns=[
    path('signup/',signup,name='signup'),
    path('logout/',logout,name='logout'),
    path('login/',loginView,name='login'),
    path('profile/<int:id>/',userProfile,name='profile'),
    path('update_user_profile/<int:id>/',updateUserProfile,name='update_user_profile'),
    path('change-password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('reset-password/', auth_views.PasswordResetView.as_view(),name='password_reset_form'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('reset-password-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view()),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)