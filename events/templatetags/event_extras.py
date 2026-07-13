from django import template

register = template.Library()

@register.filter
def sum_guests(events):
    total = 0
    for event in events:
        total += event.guest_count
    return total