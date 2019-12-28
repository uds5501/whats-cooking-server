from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import numpy as np
import json

def return_datasets(train_path, test_path):
    train = json.load(open(train_path))
    test = json.load(open(test_path))
    return (train, test)

def generate_text(dataset):
    text = [" ".join(doc['ingredients']).lower() for doc in data]
    return text

def get_tfidf_processing(train_text):
    tfidf = TfidfVectorizer(binary=True)
    train_tfidf = tfidf.fit_transform(train_text)
    train_text = train_text.astype('float16')
    return (tfidf, train_text)

def get_tfidf_input_processed(vectorizer, input_text):
    processed = vectorizer.transform(input_text)
    processed = processed('float16')
    return processed

def get_targets(train_dataset):
    return [doc['cuisine'] for doc in train_dataset]

def decode_predictions(target, encoded_prediction):
    lb = LabelEncoder()
    y = lb.fit_transform(target)
    return lb.inverse_transform(encoded_prediction)
