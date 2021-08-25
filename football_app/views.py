from django.http.response import HttpResponse
from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if "game" not in request.session:
        request.session['game'] = True
        request.session['name'] = False
        request.session['down'] = 1
        request.session['toGo'] = 10
        request.session['endZone'] = 75
    return render(request, 'index.html')
def name(request):
    request.session['name'] = request.POST['name']
    return redirect('/')

def play(request):
    if request.POST['type'] == 'run':
        runDistance = random.randint(-3,15)
        request.session['endZone'] -= runDistance
        request.session['toGo'] -= runDistance
    if request.POST['type'] == "pass":
        accuracy = random.randint(0,100)
        defense = random.randint(0,20)
        if accuracy > defense:
            passDistance = random.randint(1,25)
            request.session['endZone'] -= passDistance
            request.session['toGo'] -= passDistance
    if request.POST['type'] == 'hailmary':
        accuracy = random.randint(0,50)
        defense = random.randint(0,100)
        if accuracy > defense:
            passDistance = random.randint(35,60)
            request.session['endZone'] -= passDistance
            request.session['toGo'] -= passDistance
    if request.session['endZone'] <= 0:
        request.session['endZone'] = 0
        return HttpResponse("Touchdown")
    if request.session['toGo'] <= 0:
        request.session['toGo'] = 10
        request.session['down'] = 1
    else:
        request.session['down'] += 1
    if request.session['down'] > 4:
        return HttpResponse('Turnover on Downs')
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')
