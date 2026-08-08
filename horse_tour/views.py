from django.shortcuts import render, get_object_or_404
from .models import Location, Horse, Comment

def locations_view(request):
    locations = Location.objects.all()

    return render(request, 'locations.html', {'locations': locations})

def location_detail_view(request, id):
    location = get_object_or_404(Location, id=id)
    return render(request, 'location_detail.html', {'location': location})

def horses_view(request):
    horses = Horse.objects.all()
    return render(request, 'horses.html', {'horses': horses})
        
