from cv2 import imreadmulti
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contest(request):
    return render(request, 'contest.html')

def problems(request):
    return render(request, 'problems.html')

def submissions(request):
    return render(request, 'submissions.html')

def login(request):
    return render(request, 'login.html')
