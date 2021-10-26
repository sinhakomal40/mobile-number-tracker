from django.shortcuts import render
from tracker.forms import *
import phonenumbers as phn
from phonenumbers import timezone, geocoder, carrier

# HomePage
def home(request):
    number = []
    timeZone = []
    Carrier = []
    Region = []
    if request.method == "POST":
        form = TrackerForm(request.POST, request.FILES)
        number = request.POST.get('number', None)
        phoneNumber = phn.parse('+91'+ number)
        timeZone = timezone.time_zones_for_number(phoneNumber)
        Carrier = carrier.name_for_number(phoneNumber, 'en')
        Region = geocoder.description_for_number(phoneNumber, 'en')
    else:
        form = TrackerForm()
    return render(request, "home.html", {
        'form':form,
        'phoneNumber': number,
        'timeZone': timeZone,
        'Carrier': Carrier,
        'Region': Region
    })