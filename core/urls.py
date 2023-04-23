
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('introduce/', views.introduce, name='introduce'),
    path('csbaomat/', views.csbaomat, name='csbaomat'),
    path('dieukhoansd/', views.dieukhoansd, name='dieukhoansd'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]