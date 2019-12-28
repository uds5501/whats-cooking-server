from django.shortcuts import render
from .serializers import ResultSerializer
from .models import Result
from rest_framework import viewsets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .apps import MlConfig
from .model_processing.model_processing import process_input, decode_prediction, tfidf_transform

# Create your views here.

class ResultView(viewsets.ModelViewSet):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()

@csrf_exempt
def foobar(request):        
        if request.method == "POST":
            print(request.body.decode('utf-8'))
            print('this is a post request')
        txt = "This is an foobar challenge"
        return HttpResponse(txt)
