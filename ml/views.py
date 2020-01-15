from django.shortcuts import render
from .serializers import ResultSerializer
from .models import Result
from rest_framework import viewsets
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from .apps import MlConfig
from .model_processing.utilities import get_tfidf_input_processed, decode_predictions, generate_input_text

# Create your views here.

class ResultView(viewsets.ModelViewSet):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()

    def create(self, request):
        print("We are here in post requests")
        raise PermissionDenied

@csrf_exempt
def predict(request):
    is_text = False
    if request.method == "POST":
        input = str(request.body.decode('utf-8'))
        print(input)
        tokenised = input.split("\"")
        ing = []
        to_check = ['{', '}', ']', 'name', ':', ',', '[']
        for i in tokenised:
            flag = False
            for el in to_check:
                if el in i:
                    flag = True
                    break
            if not flag:
                ing.append(i)
        try:
            input = ' '.join(ing)
            new_object = Result(description=input)
            loaded_model = MlConfig.MODEL_OBJECT
            print(loaded_model)
            input = generate_input_text(input)
            print('input generated: \n', input)
            final_input = get_tfidf_input_processed(MlConfig.TFIDF, input)
            print('final input:', final_input)
            preds = loaded_model.predict(final_input)
            print('predicted..', preds)
            decoded_pred = decode_predictions(MlConfig.TARGETS, preds)
            txt = decoded_pred[0]
            print('prediction decoded..')
            is_text = True
            new_object.prediction = decoded_pred[0]
            new_object.save()
            print('object saved..')
        except Exception as inst:
            print(inst.args)
            print(type(inst))
            print(inst)

    if is_text:
        return HttpResponse(txt)
    else:
        return HttpResponse('MEHGGGGGGGGGGGG')