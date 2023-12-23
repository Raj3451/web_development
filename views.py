from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from .models import Pro

def projects(request):
    template = loader.get_template('project1.html')
    return HttpResponse(template.render())

def prize(request):
    project2 = Pro.objects.all().values()
    template2 = loader.get_template('prize.html')
    context ={
        'name': project2
    }
    return HttpResponse(template2.render(context,request))

def allprojects(request):
    myprojects = Pro.objects.all().values()
    template = loader.get_template('all_projects.html')
    context ={
        'myprojects':myprojects 
    }
    
    return HttpResponse(template.render(context, request))

def details(request,id):
    my_pro = Pro.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mypro' : my_pro
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
    
def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits':['Apple','Banana','Cherry'],
        
    }
    return HttpResponse(template.render(context,request))