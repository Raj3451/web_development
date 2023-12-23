from django.urls import path
from . import views

urlpatterns =[
    path('',views.main,name='main'),
    path('projects/',views.projects,name ='projects'),
    path('prize/',views.prize,name = 'prize'),
    path('allprojects/',views.allprojects,name = 'allprojects'),
    path('allprojects/details/<int:id>',views.details,name ='details'),
    path('testing/',views.testing, name ='testing')
    
]