
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('logout/',views.signout,name='signout'),
    path('login/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('dashb/',views.dashboard,name='dashboard'),
]
