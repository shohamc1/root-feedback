from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import fbcontent

# Create your views here.

def mainPage (request):
    return render (request, 'main.html')

def addfb (request):
    #create new item and save
    newitem = fbcontent(stdname=request.POST.get('stdname'), feedback=request.POST.get('message'))
    newitem.save()

    return HttpResponseRedirect ('/main/')