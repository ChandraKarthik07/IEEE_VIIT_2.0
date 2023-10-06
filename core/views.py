from django.shortcuts import render
from .models import Event,ExecutiveBody,OperatingBody,Faculty
# Create your views here.
def index(request):
    latest_events = Event.objects.order_by('-start_date')
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


def events_page(request,event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        # Handle the case where the event with the given ID does not exist
        event = None

    # Pass the event instance to the template context
    context = {'event': event}

    # Render the template with the event data
    return render(request, 'eventpage.html', context)

