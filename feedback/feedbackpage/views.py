from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import fbcontent
#import feedbackpage.cloud

# Create your views here.

def mainPage (request):
    return render (request, 'main.html')

def addfb (request):
    #create new item and save
    newitem = fbcontent(name=request.POST.get('stdname'), feedback=request.POST.get('message'), stdid=request.POST.get('stdid'), email=request.POST.get('stmail'), pillar=request.POST.get('pillar'), category=request.POST.get('category'))
    newitem.save()

    #cloud.main()
    #feedbackpage.cloud.main()

    return HttpResponseRedirect ('/main/')