from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'GIN/index.html')

def about(request):
    return render(request, 'GIN/about.html')

def auth(request):
    return HttpResponse("<h4> Authorize </h4>")

def get_started(request):
    return render(request, 'GIN/get_started.html')

def add_dataset(request):
    return render(request, 'GIN/add_dataset.html')

def analyze(request):
    return render(request, 'GIN/analyze.html')
