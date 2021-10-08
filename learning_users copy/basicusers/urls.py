from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from basicusers import views


#TEMPLATE TAGGING
app_name = 'basicusers'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login')


    


    ]