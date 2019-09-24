from django.shortcuts import render
from django.http import HttpResponseRedirect
from feedbackpage.models import fbcontent

# Create your views here.

def page(request):
    allitems = fbcontent.objects.all()
    category = request.session.get('category')
    return render (request, 'submissions.html', {'allitems': allitems, 'category': category})

def categoryfn(request):
    request.session['category'] = request.POST.get('cat')
    return HttpResponseRedirect('/submissions/')

#None is generated when category is empty