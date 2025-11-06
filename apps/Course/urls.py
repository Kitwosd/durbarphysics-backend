from django.urls import path
from . import views


urlpatterns = [
    path('users/add/', views.add_user, name='add_user'),
    path('academic-levels/add/', views.add_academic_level, name='add_academic_level'),
    path('streams/add/', views.add_stream, name='add_stream'),
    path('subjects/add/', views.add_subject, name='add_subject'),
    path('enrollments/add/', views.add_enrollment, name='add_enrollment'),
    path('live-classes/add/', views.add_live_class, name='add_live_class'),
    path('activities/add/', views.add_activity, name='add_activity'),
    path('videos/add/', views.add_video, name='add_video'),


    
    
    # List URLs
    path('subjects/', views.subject_list, name='subject_list'),
]