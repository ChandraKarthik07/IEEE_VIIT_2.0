from django.shortcuts import render
from .models import Event,ExecutiveBody,OperatingBody,Faculty
# Create your views here.
def index(request):
    latest_events = Event.objects.order_by('-date')
    context = {'events': latest_events}


    return render(request, 'index.html',context)
def profile(request):
    executive_bodies = ExecutiveBody.objects.all().order_by('level')
    operating_bodies = OperatingBody.objects.all().order_by('level')

    faculty_members = Faculty.objects.all().order_by('level')

    context = {
        'executive_bodies': executive_bodies,
        'operating_bodies': operating_bodies,
        'faculty_members': faculty_members,
    }

    return render(request, 'profile.html',context)   



