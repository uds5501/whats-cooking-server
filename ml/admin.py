from django.contrib import admin
from .models import Result
# Register your models here.

class ResultAdmin(admin.ModelAdmin):
    list_display = ('description', 'prediction', 'confidence', 'is_correct', 'other_predcitions')

admin.site.register(Result, ResultAdmin)
