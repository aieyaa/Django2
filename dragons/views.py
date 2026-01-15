from django.shortcuts import render

from dragons.serializers import DragonSerializer
from .models import Dragon
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import filters as filter


def liste_dragons(request):
    dragons = Dragon.objects.all()
    return render(request, "dragons/liste_dragons.html", {
        "dragons": dragons
    })

def home(request):
    return HttpResponse("Bienvenue sur le site des dragons !") 

class DragonViewSet(viewsets.ModelViewSet):
    queryset = Dragon.objects.all()
    serializer_class = DragonSerializer
    filter_backends = [filter.SearchFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'age']