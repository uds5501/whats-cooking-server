from django.db import models

# Create your models here.
class Result(models.Model):

    description = models.TextField()
    prediction = models.CharField(max_length=50)
    is_correct = models.BooleanField(null=True)

    def __str__(self):
        return self.description + ' : ' + self.prediction
