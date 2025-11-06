from .utility import get_all_streams, get_all_users, get_all_subjects, get_all_extra_curricular_activities,get_all_academic_levels, get_all_live_classes,get_all_videos
def all_users_processor(request):
    return get_all_users()

from datetime import datetime as time

def all_subjects_processor(request):
    return get_all_subjects()

def all_extra_curricular_activities_processor(request):
    return get_all_extra_curricular_activities()

def current_path(request):
    print(f"---------------------Request Path:: {request.path}---------------------")
    print(request.user if request.user.is_authenticated else "Developer")
    return {'current_path': request.path}

def get_all_classes_processor(request):
    return get_all_academic_levels()

def get_all_streams_processor(request):
    return get_all_streams()

def get_all_live_classes_processor(request):
    return get_all_live_classes()

def get_all_videos_processor(request):
    return get_all_videos()
