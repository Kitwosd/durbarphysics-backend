from .models import Video
from .models import Stream
from .models import AcademicLevel
from .models import User, Subject, ExtraCurricularActivity
# importing redis cache library
from django.core.cache import cache
from django.db.models import Count
from .models import LiveClass






def get_all_users():
    # Fetch all users once
    all_users = User.objects.all()

    # Count users by role
    queryset_results = all_users.values('role').annotate(user_count=Count('role'))
    role_counts = {item['role']: item['user_count'] for item in queryset_results}
    
    total_users = sum(role_counts.values())
    admin_count = role_counts.get(User.Role.ADMIN, 0)
    teacher_count = role_counts.get(User.Role.TEACHER, 0)
    student_count = role_counts.get(User.Role.STUDENT, 0)

    # Separate lists using Python filtering (no new DB query)
    teachers = [user for user in all_users if user.role == User.Role.TEACHER]
    students = [user for user in all_users if user.role == User.Role.STUDENT]

    context = {
        'total': total_users,
        'admin_count': admin_count,
        'teacher_count': teacher_count,
        'student_count': student_count,
        'teachers': teachers,
        'students': students,
    }

    return context

def get_all_subjects():
    subjects = Subject.objects.all()
    subject_count = subjects.count()

    limited_subjects = subjects[:3]  

    context = {
        'subjects': subjects,
        'subject_count': subject_count,
        'limited_subjects': limited_subjects
    }
    print("total subjects::", subject_count)
    return context

def get_all_extra_curricular_activities():
    extra_activities = ExtraCurricularActivity.objects.all()
    extra_activity_count = extra_activities.count()
    limited_activities = extra_activities[:3]
    context = {
        'extra_activities': extra_activities,
        'extra_activity_count': extra_activity_count,
        'limited_activities': limited_activities
    }
    return context
    
def get_all_academic_levels():
    levels = AcademicLevel.objects.all()
    level_count = levels.count()
    limited_levels = levels.order_by('-pk')[:3]
    # return 0 if capacity_remaining is None else capacity_remaining
    capacity_remaining = [level.capacity_remaining() for level in limited_levels if level.capacity_remaining() is not None]
    context = {
        'levels': levels,
        'level_count': level_count,
        'limited_levels': limited_levels,
        'capacity_remaining': capacity_remaining
    }
    return context

def get_all_streams():
    streams = Stream.objects.all()
    stream_count = streams.count()
    limited_streams = streams.order_by('-pk')[:3]
    context = {
        'streams': streams,
        'stream_count': stream_count,
        'limited_streams': limited_streams
    }
    return context

def get_all_live_classes():
    live_classes = LiveClass.objects.all()
    live_class_count = live_classes.count()
    limited_live_classes = live_classes.order_by('-pk')[:3]

    context = {
        'live_classes': live_classes,
        'live_class_count': live_class_count,
        'limited_live_classes': limited_live_classes
    }
    return context

def get_all_videos():
    videos = Video.objects.all()
    video_count = videos.count()
    limited_videos = videos.order_by('-pk')[:3]
    print('---')
    for video in videos:
        print(f'Video ID: {video.id}, Title: {video.title}')
        # ManyToMany field - need to use .all() to get the related streams
        streams = video.stream.all()
        if streams.exists():
            stream_names = ', '.join([stream.name for stream in streams])
            print(f'streams: {stream_names}')
        else:
            print(f'streams: None assigned')
    print('---')
    context = {
        'videos': videos,
        'video_count': video_count,
        'limited_videos': limited_videos
    }
    return context