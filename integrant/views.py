from django.http import HttpResponse
from django.shortcuts import render

from integrant.models import Integrant

def create_integrants(request):
    new_integrant=Integrant.objects.create(name ='Tomas Agustin', edge =25 , major = True)
    print(new_integrant)
    return HttpResponse('nuevo integrante creado')

def list_integrants(request):
    all_integrants =Integrant.objects.all
    print(all_integrants)
    context = {
        'integrant': all_integrants,        
    }
    return render(request,'list_integrants.html',context=context)