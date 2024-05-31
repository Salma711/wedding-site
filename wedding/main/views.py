from django.shortcuts import render, get_object_or_404
from .models import *

def main(request):
    return render(request, 'main.html')
def check_band_availability(request, band_id, date):
    band = Band.objects.get(pk=band_id)
    availability = band.is_available_on_date(date)
    return render(request, 'band.html', {'band': band, 'date': date, 'availability': availability})
def band(request):
    bands = Band.objects.all()
    return render(request, 'band.html', {'bands': bands})
def cake(request):
    images = Cake.objects.all()
    return render(request, 'cake.html', {'images': images})
def photographer(request):
    images = Photographer.objects.all()
    return render(request, 'photographer.html', {'images': images})
def dress(request):
    images = Dress.objects.all()
    return render(request, 'dress.html', {'images': images})
def venue(request):
    images = Venue.objects.all()
    return render(request, 'venue.html', {'images': images})
def flower(request):
    images = Flower.objects.all()
    return render(request, 'flower.html', {'images': images})



