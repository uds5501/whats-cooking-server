from django.apps import AppConfig
import json
import os

class MlConfig(AppConfig):
    name = 'ml'
    print("LOADING MODEL...")    
    # Perform whole processing sequentially
