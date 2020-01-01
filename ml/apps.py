from django.apps import AppConfig
from sklearn.externals import joblib
from .model_processing.utilities import return_datasets, generate_text, get_tfidf_input_processed, get_tfidf_processing, get_targets, decode_predictions
import json
import os

class MlConfig(AppConfig):
    name = 'ml'
    # Preprocess essential inputs    
    BASE_PATH = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model_processing'), 'input')
    MODEL_WEIGHT = os.path.join(BASE_PATH, 'final_model.sav')
    TRAIN_DATA = os.path.join(BASE_PATH, 'train.json')
    TEST_DATA = os.path.join(BASE_PATH, 'test.json')

    MODEL_OBJECT = joblib.load(MODEL_WEIGHT)
    TRAIN_DATASET, TEST_DATASET = return_datasets(TRAIN_DATA, TEST_DATA)

    TRAIN_TEXT = generate_text(TRAIN_DATASET)
    TFIDF, TRAIN_TEXT = get_tfidf_processing(TRAIN_TEXT)

    TARGETS = get_targets(TRAIN_DATASET)
