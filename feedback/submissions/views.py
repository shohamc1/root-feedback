from django.shortcuts import render
from feedbackpage.models import fbcontent

# Create your views here.

def page(request):
    allitems = fbcontent.objects.all()
    return render (request, 'submissions.html', {'allitems': allitems})
