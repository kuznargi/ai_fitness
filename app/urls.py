from django.urls import path,include 
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('select-goal/', goal_selection_view, name='select_goal'),
    path('workout/', workout_view, name='workout_screen'), 
    path('results/', results_view, name='results_screen'),
    path('program-dashboard/', program_dashboard_view, name='program_dashboard'),
] 