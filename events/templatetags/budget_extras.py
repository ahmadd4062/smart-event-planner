from django import template

register = template.Library()

@register.filter
def get_category_label(category):
    labels = {
        'venue': 'Venue',
        'catering': 'Catering',
        'entertainment': 'Entertainment',
        'decor': 'Decorations',
        'transport': 'Transportation',
        'staff': 'Staff',
        'marketing': 'Marketing',
        'other': 'Other',
    }
    return labels.get(category, category)