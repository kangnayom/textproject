from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import HttpResponse
from core.models import Syllabus
from soynlp.noun import LRNounExtractor
from django.http import HttpResponse



def syllabus_check(request):
    results = []
    for s in Syllabus.objects.all():
        results.append(f"<h3>{s.title}</h3><p>{s.content[:300]}...</p>")
    return HttpResponse("<hr>".join(results))

def home(request):
    return HttpResponse("Hello, this is the main page!")



from .forms import TimetableForm

def timetable_register(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TimetableForm()
    return render(request, 'timetable_register.html', {'form': form})
