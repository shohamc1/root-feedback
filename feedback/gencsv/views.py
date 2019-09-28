import csv
from django.shortcuts import HttpResponse
from feedbackpage.models import fbcontent

# Create your views here.

def createcsv(request):
    response = HttpResponse(content_type='text/csv')
    meta = fbcontent._meta
    field_names = [field.name for field in meta.fields]

    writer = csv.writer(response)

    writer.writerow(field_names)

    for obj in fbcontent.objects.all():
        writer.writerow([getattr(obj, field) for field in field_names])

    response['Content-Disposition'] = 'attachment; filename="feedback.csv"'
    return response