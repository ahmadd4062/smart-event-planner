from django.urls import path
from . import views

urlpatterns = [
    # Event URLs
    path('', views.event_list, name='event_list'),
    path('create/', views.event_create, name='event_create'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('<int:pk>/delete/', views.event_delete, name='event_delete'),
    
    # Guest URLs
    path('<int:event_id>/guests/', views.guest_list, name='guest_list'),
    path('<int:event_id>/guests/add/', views.guest_add, name='guest_add'),
    path('guests/<int:pk>/edit/', views.guest_edit, name='guest_edit'),
    path('guests/<int:pk>/delete/', views.guest_delete, name='guest_delete'),
    
    # Budget URLs
    path('<int:event_id>/budget/', views.budget_view, name='budget_view'),
    path('<int:event_id>/expenses/add/', views.expense_add, name='expense_add'),
    path('expenses/<int:pk>/edit/', views.expense_edit, name='expense_edit'),
    path('expenses/<int:pk>/delete/', views.expense_delete, name='expense_delete'),
    
    # Timeline URLs
    path('<int:event_id>/timeline/', views.timeline_view, name='timeline_view'),
    path('<int:event_id>/tasks/add/', views.task_add, name='task_add'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('tasks/<int:pk>/status/<str:status>/', views.task_status_update, name='task_status_update'),
]