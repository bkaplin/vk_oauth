from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
import vk
from django.contrib.auth.models import User

def home(request):
    if request.user in User.objects.all():
        user = request.user
        token = user.social_auth.first().extra_data['access_token']
        uid = user.social_auth.first().uid

        session = vk.Session(access_token=token)
        vkapi = vk.API(session)
        friends_ids_list = vkapi.friends.get(user_id=uid, v=2, count=5)
        friends_list = []
        for friend_id in friends_ids_list:
            name = vkapi.users.get(user_id=friend_id, v=2)
            name = " ".join([name[0]['first_name'], name[0]['last_name']])
            friends_list.append(name)
        context = {'friends': friends_list}
    else:
        context = {}
    return render(request, 'home.html', context)

def logout(request):
    auth_logout(request)
    return redirect('/')
