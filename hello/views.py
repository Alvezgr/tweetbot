from django.shortcuts import render
from django.http import HttpResponse
from .tweetbot import update_status

from .models import Greeting

# Create your views here.
def index(request):
	#d = update_status()
    d = update_status()
    # return HttpResponse('Hello from Python!')
    return render(request, 'twittear.html',{'d': d})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

