from django.urls import path
from .views import signup,logout,loginView

urlpatterns=[
    path('signup/',signup,name='signup'),
    path('logout/',logout,name='logout'),
    path('login/',loginView,name='login'),
]