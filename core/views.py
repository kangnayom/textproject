from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from core.models import Syllabus

def syllabus_check(request):
    results = []
    for s in Syllabus.objects.all():
        results.append(f"<h3>{s.title}</h3><p>{s.content[:300]}...</p>")
    return HttpResponse("<hr>".join(results))

