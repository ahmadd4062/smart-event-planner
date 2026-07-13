from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Guest, Expense, TimelineTask


@login_required
def event_list(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'events/list.html', {'events': events})

@login_required
def event_create(request):
    if request.method == 'POST':
        event = Event.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            event_type=request.POST.get('event_type'),
            description=request.POST.get('description'),
            event_date=request.POST.get('event_date'),
            location=request.POST.get('location'),
            guest_count=request.POST.get('guest_count', 0),
            budget=request.POST.get('budget', 0),
            status=request.POST.get('status', 'planning')
        )
        messages.success(request, 'Event created successfully!')
        return redirect('event_detail', pk=event.pk)
    return render(request, 'events/create.html')

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    return render(request, 'events/detail.html', {'event': event})

@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    
    if request.method == 'POST':
        event.name = request.POST.get('name')
        event.event_type = request.POST.get('event_type')
        event.description = request.POST.get('description')
        event.event_date = request.POST.get('event_date')
        event.location = request.POST.get('location')
        event.guest_count = request.POST.get('guest_count', 0)
        event.budget = request.POST.get('budget', 0)
        event.status = request.POST.get('status', 'planning')
        event.save()
        
        messages.success(request, 'Event updated successfully!')
        return redirect('event_detail', pk=event.pk)
    
    return render(request, 'events/edit.html', {'event': event})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('event_list')
    return render(request, 'events/delete.html', {'event': event})


@login_required
def guest_list(request, event_id):
    event = get_object_or_404(Event, pk=event_id, user=request.user)
    guests = Guest.objects.filter(event=event)
    
    # RSVP statistics
    stats = {
        'total': guests.count(),
        'confirmed': guests.filter(rsvp_status='confirmed').count(),
        'pending': guests.filter(rsvp_status='pending').count(),
        'declined': guests.filter(rsvp_status='declined').count(),
        'maybe': guests.filter(rsvp_status='maybe').count(),
    }
    
    context = {
        'event': event,
        'guests': guests,
        'stats': stats,
    }
    return render(request, 'events/guest_list.html', context)

@login_required
def guest_add(request, event_id):
    event = get_object_or_404(Event, pk=event_id, user=request.user)
    
    if request.method == 'POST':
        Guest.objects.create(
            event=event,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            rsvp_status=request.POST.get('rsvp_status', 'pending'),
            notes=request.POST.get('notes')
        )
        messages.success(request, 'Guest added successfully!')
        return redirect('guest_list', event_id=event.pk)
    
    return render(request, 'events/guest_add.html', {'event': event})

@login_required
def guest_edit(request, pk):
    guest = get_object_or_404(Guest, pk=pk, event__user=request.user)
    
    if request.method == 'POST':
        guest.name = request.POST.get('name')
        guest.email = request.POST.get('email')
        guest.phone = request.POST.get('phone')
        guest.rsvp_status = request.POST.get('rsvp_status', 'pending')
        guest.notes = request.POST.get('notes')
        guest.save()
        
        messages.success(request, 'Guest updated successfully!')
        return redirect('guest_list', event_id=guest.event.pk)
    
    return render(request, 'events/guest_edit.html', {'guest': guest})

@login_required
def guest_delete(request, pk):
    guest = get_object_or_404(Guest, pk=pk, event__user=request.user)
    event_id = guest.event.pk
    
    if request.method == 'POST':
        guest.delete()
        messages.success(request, 'Guest deleted successfully!')
        return redirect('guest_list', event_id=event_id)
    
    return render(request, 'events/guest_delete.html', {'guest': guest})


@login_required
def budget_view(request, event_id):
    event = get_object_or_404(Event, pk=event_id, user=request.user)
    expenses = Expense.objects.filter(event=event)
    
    # Calculate totals by category
    total_spent = 0
    category_totals = {}
    
    for expense in expenses:
        total_spent += float(expense.amount)  # Convert to float
        if expense.category in category_totals:
            category_totals[expense.category] += float(expense.amount)
        else:
            category_totals[expense.category] = float(expense.amount)
    
    # Convert budget to float for calculations
    budget_float = float(event.budget)
    
    # Budget remaining
    budget_remaining = budget_float - total_spent
    
    # Percentage used
    percentage_used = 0
    if budget_float > 0:
        percentage_used = (total_spent / budget_float) * 100
    
    context = {
        'event': event,
        'expenses': expenses,
        'total_spent': total_spent,
        'category_totals': category_totals,
        'budget_remaining': budget_remaining,
        'percentage_used': percentage_used,
    }
    return render(request, 'events/budget.html', context)

@login_required
def expense_add(request, event_id):
    event = get_object_or_404(Event, pk=event_id, user=request.user)
    
    if request.method == 'POST':
        Expense.objects.create(
            event=event,
            category=request.POST.get('category'),
            description=request.POST.get('description'),
            amount=request.POST.get('amount'),
            notes=request.POST.get('notes')
        )
        messages.success(request, 'Expense added successfully!')
        return redirect('budget_view', event_id=event.pk)
    
    return render(request, 'events/expense_add.html', {'event': event})

@login_required
def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk, event__user=request.user)
    
    if request.method == 'POST':
        expense.category = request.POST.get('category')
        expense.description = request.POST.get('description')
        expense.amount = request.POST.get('amount')
        expense.notes = request.POST.get('notes')
        expense.save()
        
        messages.success(request, 'Expense updated successfully!')
        return redirect('budget_view', event_id=expense.event.pk)
    
    return render(request, 'events/expense_edit.html', {'expense': expense})

@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk, event__user=request.user)
    event_id = expense.event.pk
    
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
        return redirect('budget_view', event_id=event_id)
    
    return render(request, 'events/expense_delete.html', {'expense': expense})


@login_required
def timeline_view(request, event_id):
    event = get_object_or_404(Event, pk=event_id, user=request.user)
    tasks = TimelineTask.objects.filter(event=event)
    
    # Status counts
    status_counts = {
        'not_started': tasks.filter(status='not_started').count(),
        'in_progress': tasks.filter(status='in_progress').count(),
        'completed': tasks.filter(status='completed').count(),
        'delayed': tasks.filter(status='delayed').count(),
        'cancelled': tasks.filter(status='cancelled').count(),
    }
    
    context = {
        'event': event,
        'tasks': tasks,
        'status_counts': status_counts,
    }
    return render(request, 'events/timeline.html', context)

@login_required
def task_add(request, event_id):
    event = get_object_or_404(Event, pk=event_id, user=request.user)
    
    if request.method == 'POST':
        task = TimelineTask.objects.create(
            event=event,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
            status=request.POST.get('status', 'not_started'),
            order=TimelineTask.objects.filter(event=event).count() + 1
        )
        messages.success(request, 'Task added to timeline!')
        return redirect('timeline_view', event_id=event.pk)
    
    return render(request, 'events/task_add.html', {'event': event})

@login_required
def task_edit(request, pk):
    task = get_object_or_404(TimelineTask, pk=pk, event__user=request.user)
    
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.start_date = request.POST.get('start_date')
        task.end_date = request.POST.get('end_date')
        task.status = request.POST.get('status', 'not_started')
        task.save()
        
        messages.success(request, 'Task updated successfully!')
        return redirect('timeline_view', event_id=task.event.pk)
    
    return render(request, 'events/task_edit.html', {'task': task})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(TimelineTask, pk=pk, event__user=request.user)
    event_id = task.event.pk
    
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('timeline_view', event_id=event_id)
    
    return render(request, 'events/task_delete.html', {'task': task})

@login_required
def task_status_update(request, pk, status):
    task = get_object_or_404(TimelineTask, pk=pk, event__user=request.user)
    
    if status in ['not_started', 'in_progress', 'completed', 'delayed', 'cancelled']:
        task.status = status
        task.save()
        messages.success(request, f'Task status updated to {task.get_status_display()}')
    
    return redirect('timeline_view', event_id=task.event.pk)