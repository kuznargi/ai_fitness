from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import urllib


def index(request):
    return render(request, 'index.html') 

def goal_selection_view(request):
    if request.method == 'POST':
        goal = request.POST.get('goal')
        fitness_level = request.POST.get('fitness_level')
        workout_frequency = request.POST.get('workout_frequency')

        # Process medical conditions checkboxes
        med_conditions_list = []
        if request.POST.get('med_joints') == 'true':
            med_conditions_list.append('Проблемы с суставами')
        if request.POST.get('med_cardio') == 'true':
            med_conditions_list.append('Сердечно-сосудистые заболевания')
        if request.POST.get('med_recent_injury') == 'true':
            med_conditions_list.append('Недавние травмы или операции')
        if request.POST.get('med_pregnancy') == 'true':
            med_conditions_list.append('Беременность или послеродовой период')
        
        med_other_details = request.POST.get('med_other_details', '').strip()
        if med_other_details:
            med_conditions_list.append(f'Другое: {med_other_details}')
        
        # Join all collected medical conditions into a single string or handle as a list
        health_conditions_str = ", ".join(med_conditions_list) if med_conditions_list else "Нет"

        # Process preferred exercise types checkboxes
        preferred_exercises_list = []
        if request.POST.get('pref_cardio') == 'true':
            preferred_exercises_list.append('Кардио')
        if request.POST.get('pref_strength') == 'true':
            preferred_exercises_list.append('Силовые тренировки')
        if request.POST.get('pref_yoga_pilates') == 'true':
            preferred_exercises_list.append('Йога и пилатес')
        if request.POST.get('pref_stretching') == 'true':
            preferred_exercises_list.append('Растяжка и гибкость')
            
        preferred_exercises_str = ", ".join(preferred_exercises_list) if preferred_exercises_list else "Не указаны"

       

       
        params = {
            'goal': goal,
            'fitness_level': fitness_level,
            'health_conditions': health_conditions_str,
            'workout_frequency': workout_frequency,
            'preferred_exercises': preferred_exercises_str
        }
        query_string = urllib.parse.urlencode(params)
        # Redirect to the program dashboard screen with data as query parameters
        return redirect(reverse('program_dashboard') + '?' + query_string)
    else:
        # GET request, just render the form
        return render(request, 'goal_selection.html')

def workout_view(request):
    # We can extract the parameters here if needed for server-side logic later
    # For now, the template handles them with JavaScript
    return render(request, 'workout_screen.html')

def results_view(request):
   return render(request, 'results_screen.html')

def program_dashboard_view(request):
    context = {
        'goal': request.GET.get('goal'),
        'fitness_level': request.GET.get('fitness_level'),
        'health_conditions': request.GET.get('health_conditions'),
        'workout_frequency': request.GET.get('workout_frequency'),
        'preferred_exercises': request.GET.get('preferred_exercises'),
    }
    # print("Dashboard Context:", context) # For debugging if needed
    return render(request, 'program_dashboard.html', context)

def goal_selection_view(request):
    return HttpResponse("Форма загружается")