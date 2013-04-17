from django.shortcuts import render
from models import Poll


def show_all_pools(request):
    polls = Poll.objects.all()
    return render(request, 'all_polls.html', {'polls': polls, })


def poll(request, poll_id):
    return None