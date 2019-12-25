from django.shortcuts import render
from .serializers import ResultSerializer
from .models import Result
from rest_framework import viewsets
from django.http import HttpResponse

# Create your views here.

class ResultView(viewsets.ModelViewSet):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()

def foobar(request):
    txt = "This is an foobar challenge: {}".format(simpleId)
    return HttpResponse(txt)
