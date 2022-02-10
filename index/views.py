from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def project(request):
    return HttpResponse('<h1>mario es gay</h1>')


