from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def index(request):
    return render(request, 'chat/index.html', {})

# @login_required
def room(request, room_name):
    # username_str = None
    # username=request.session['username']
    # if(username.is_authenticated()):
    #     username_str = username.username
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        # 'username':username,
    })
