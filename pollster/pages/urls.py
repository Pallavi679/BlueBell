from django.contrib import admin
from django.urls import path
from pollster import urls
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('poll/',views.poll, name='poll'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logoutUser, name='logout'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),

]
