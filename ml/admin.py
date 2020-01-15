from django.contrib import admin
from .models import Result
# Register your models here.

class ResultAdmin(admin.ModelAdmin):
    list_display = ('description', 'prediction', 'is_correct')

admin.site.register(Result, ResultAdmin)
