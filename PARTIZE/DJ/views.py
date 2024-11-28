from django.shortcuts import render
from .models import Event
from .forms import EventForm

# Create your views here.
def home(request):
    all_event = Event.objects.all
    return render(request, 'home.html', {
        'all':all_event
    })

# def add_event(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         date = request.POST['date']
#         venue = request.POST['venue']
#         manager = request.POST['manager']
#         description = request.POST['description']

#         event = Event(name=name, date=date, venue=venue, manager=manager, description=description)
#         event.save()

#         return render(request, 'home.html', {
#             'all':Event.objects.all
#         })
#     else:
#         return render(request, 'add_event.html')

def add_event(request):
    form = EventForm
    return render(request, 'add_event.html',{ 'form':form})