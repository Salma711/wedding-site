from django.db import models
from django.contrib.auth.models import User

class Cake(models.Model):
    size = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default= 0, null=False, blank=False, upload_to='images/')
class Band(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default= 0, null=False, blank=False, upload_to='images/')
    def is_available_on_date(self, date):
        return not self.bookings.filter(date=date).exists()
class Band_Booking(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
class Cake_Booking(models.Model):
    Cake = models.ForeignKey(Cake, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
class Photographer(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(default= 0, null=False, blank=False, upload_to='images/')
    def is_available_on_date(self, date):
        return not self.bookings.filter(date=date).exists()
class Photographer_Booking (models.Model):
    Photographer= models.ForeignKey(Photographer, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
class Dress(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default= 0, null=False, blank=False, upload_to='images/')
    def is_available_on_date(self, date):
        return not self.bookings.filter(date=date).exists()
class Dress_Booking(models.Model):
    dress=models.ForeignKey(Dress,on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
class Venue(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default= 0, null=False, blank=False, upload_to='images/')
    options =[
        ('option1', 'Open Venue'),
        ('option2', 'Closed Venue'),
    ]
    type = models.CharField(max_length=10, choices=options, default='option2')
    def is_available_on_date(self, date):
        return not self.bookings.filter(date=date).exists()
class Venue_Booking(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
class Flower(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default= 0, null=False, blank=False, upload_to='images/')
    name = models.CharField(max_length=255)
class Flower_Booking(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()