from django.shortcuts import render

def index(request):
    return render (request, 'h_core/index.html')