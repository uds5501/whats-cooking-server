from django.shortcuts import render
from .serializers import ResultSerializer
from .models import Result
from rest_framework import viewsets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class ResultView(viewsets.ModelViewSet):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()

@csrf_exempt
def foobar(request):
    print(request)
    if request.method == "POST":
        print(request.body.decode('utf-8'))
        print('this is a post request')
    txt = "This is an foobar challenge"
    return HttpResponse(txt)
