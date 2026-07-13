import google.generativeai as genai
from django.conf import settings
import json
import re

# Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)

def get_event_recommendations(event):
    """
    Get AI recommendations for venues, catering, and entertainment
    """
    prompt = f"""
    Provide recommendations for an event with the following details:
    
    Event Name: {event.name}
    Event Type: {event.get_event_type_display()}
    Guest Count: {event.guest_count}
    Budget: ${event.budget}
    Location: {event.location}
    Description: {event.description or 'No description provided'}
    
    Please provide 3 recommendations each for:
    1. Venues (suitable locations for this event)
    2. Catering (food services appropriate for this event)
    3. Entertainment (activities/performers suitable for this event)
    
    For each recommendation, provide:
    - name
    - description
    - cost (estimated in dollars)
    - contact (phone or email)
    - rating (out of 5)
    - address (for venues) or cuisine_type (for catering) or type (for entertainment)
    
    Format your response as a JSON object with keys: venues, catering, entertainment.
    Each should be a list of objects with the fields mentioned above.
    """
    
    try:
        model = genai.GenerativeModel('gemini-3.5-flash')
        response = model.generate_content(prompt)
        
        # Extract JSON from response
        content = response.text
        json_match = re.search(r'\{.*\}', content, re.DOTALL)
        
        if json_match:
            data = json.loads(json_match.group())
            return data
        else:
            # Fallback recommendations if JSON parsing fails
            return get_fallback_recommendations(event)
            
    except Exception as e:
        print(f"AI Error: {e}")
        return get_fallback_recommendations(event)

def get_fallback_recommendations(event):
    """
    Return sample recommendations if AI fails
    """
    event_type = event.event_type
    guest_count = event.guest_count
    budget = float(event.budget) if event.budget else 1000
    
    # Sample venues
    venues = [
        {
            'name': 'Grand Plaza Hotel',
            'description': f'Perfect {event_type} venue with excellent facilities',
            'cost': budget * 0.4,
            'contact': 'grandplaza@hotel.com',
            'rating': 4.5,
            'address': '123 Main Street, City'
        },
        {
            'name': 'Garden View Hall',
            'description': 'Beautiful outdoor and indoor space',
            'cost': budget * 0.3,
            'contact': 'gardenview@events.com',
            'rating': 4.2,
            'address': '456 Park Avenue, City'
        },
        {
            'name': 'City Convention Center',
            'description': 'Large capacity venue for big events',
            'cost': budget * 0.5,
            'contact': 'citycenter@convention.com',
            'rating': 4.0,
            'address': '789 Convention Blvd, City'
        }
    ]
    
    # Sample catering
    catering = [
        {
            'name': 'Gourmet Delights',
            'description': f'Excellent {event_type} catering services',
            'cost': budget * 0.25,
            'contact': 'gourmet@catering.com',
            'rating': 4.7,
            'cuisine_type': 'International'
        },
        {
            'name': 'Local Flavors',
            'description': 'Authentic local cuisine for your event',
            'cost': budget * 0.2,
            'contact': 'local@flavors.com',
            'rating': 4.3,
            'cuisine_type': 'Local'
        },
        {
            'name': 'Sweet Treats Bakery',
            'description': 'Desserts and pastries for special events',
            'cost': budget * 0.15,
            'contact': 'sweet@treats.com',
            'rating': 4.4,
            'cuisine_type': 'Bakery/Desserts'
        }
    ]
    
    # Sample entertainment
    entertainment = [
        {
            'name': 'Star DJ Entertainment',
            'description': 'Professional DJ and music services',
            'cost': budget * 0.2,
            'contact': 'stardj@entertainment.com',
            'rating': 4.6,
            'type': 'Music/DJ'
        },
        {
            'name': 'Comedy Central',
            'description': 'Stand-up comedy for your event',
            'cost': budget * 0.15,
            'contact': 'comedy@central.com',
            'rating': 4.1,
            'type': 'Comedy'
        },
        {
            'name': 'Magic Moments',
            'description': 'Professional magician and illusionist',
            'cost': budget * 0.18,
            'contact': 'magic@moments.com',
            'rating': 4.3,
            'type': 'Magic'
        }
    ]
    
    return {
        'venues': venues,
        'catering': catering,
        'entertainment': entertainment
    }