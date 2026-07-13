from django.db import models
from django.contrib.auth.models import User
from events.models import Event

class VenueRecommendation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='venue_recommendations')
    name = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=200, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    address = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.event.name}"

class CateringRecommendation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='catering_recommendations')
    name = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=200, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    cuisine_type = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.event.name}"

class EntertainmentRecommendation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='entertainment_recommendations')
    name = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=200, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    type = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.event.name}"