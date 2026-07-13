from django.urls import path
from . import views

urlpatterns = [
    path('event/<int:event_id>/', views.recommendations_view, name='recommendations'),
    path('event/<int:event_id>/generate/', views.generate_recommendations, name='generate_recommendations'),
]