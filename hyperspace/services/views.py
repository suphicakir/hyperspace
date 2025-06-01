from django.shortcuts import render
from . models import Services

# Create your views here.
def services_list(request):
    services=Services.objects.all()

    return render (request,'services/services_list.html',{'services':services})
