from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from events.models import Event
from .models import VenueRecommendation, CateringRecommendation, EntertainmentRecommendation
from utils.ai_helper import get_event_recommendations

@login_required
def recommendations_view(request, event_id):
    event = get_object_or_404(Event, pk=event_id, user=request.user)
    
    venues = VenueRecommendation.objects.filter(event=event)
    caterings = CateringRecommendation.objects.filter(event=event)
    entertainments = EntertainmentRecommendation.objects.filter(event=event)
    
    context = {
        'event': event,
        'venues': venues,
        'caterings': caterings,
        'entertainments': entertainments,
    }
    return render(request, 'recommendations/view.html', context)

@login_required
def generate_recommendations(request, event_id):
    event = get_object_or_404(Event, pk=event_id, user=request.user)
    
    if request.method == 'POST':
        # Call AI helper to get recommendations
        recommendations = get_event_recommendations(event)
        
        # Clear existing recommendations
        VenueRecommendation.objects.filter(event=event).delete()
        CateringRecommendation.objects.filter(event=event).delete()
        EntertainmentRecommendation.objects.filter(event=event).delete()
        
        # Save venue recommendations
        for venue in recommendations.get('venues', []):
            VenueRecommendation.objects.create(
                event=event,
                name=venue.get('name', ''),
                description=venue.get('description', ''),
                cost=venue.get('cost', 0),
                contact=venue.get('contact', ''),
                rating=venue.get('rating', 0),
                address=venue.get('address', '')
            )
        
        # Save catering recommendations
        for catering in recommendations.get('catering', []):
            CateringRecommendation.objects.create(
                event=event,
                name=catering.get('name', ''),
                description=catering.get('description', ''),
                cost=catering.get('cost', 0),
                contact=catering.get('contact', ''),
                rating=catering.get('rating', 0),
                cuisine_type=catering.get('cuisine_type', '')
            )
        
        # Save entertainment recommendations
        for entertainment in recommendations.get('entertainment', []):
            EntertainmentRecommendation.objects.create(
                event=event,
                name=entertainment.get('name', ''),
                description=entertainment.get('description', ''),
                cost=entertainment.get('cost', 0),
                contact=entertainment.get('contact', ''),
                rating=entertainment.get('rating', 0),
                type=entertainment.get('type', '')
            )
        
        messages.success(request, 'AI recommendations generated successfully!')
        return redirect('recommendations', event_id=event.pk)
    
    return redirect('recommendations', event_id=event.pk)