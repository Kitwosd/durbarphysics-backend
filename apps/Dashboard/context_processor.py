


def messages_processor(request):
    return {
        'messages': [message for message in request._messages] or None
    }

def current_user_details(request):
    user = request.user
    message = user.username if user.is_authenticated else 'Guest'
    return {
        'current_user': user,
        'profile_image_url': user.profile.image.url if user and user.profile.image else None,
        'message': message
    }

