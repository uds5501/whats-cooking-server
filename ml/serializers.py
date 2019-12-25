from rest_framework import serializers
from .models import Result

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'description', 'prediction', 'confidence', 'is_correct', 'other_predictions')
