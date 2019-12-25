from django.db import models

# Create your models here.
class Result(models.Model):

    description = models.TextField()
    prediction = models.CharField(max_length=50)
    confidence = models.FloatField()
    is_correct = models.BooleanField(null=True)
    other_predictions = models.TextField()

    def __str__(self):
        return self.description + ' : ' + self.prediction
