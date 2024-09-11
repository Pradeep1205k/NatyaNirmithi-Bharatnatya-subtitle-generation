# src/evaluate.py
import numpy as np
import joblib
from sklearn.metrics import classification_report

def evaluate_model(model_path, features, labels):
    model = joblib.load(model_path)
    y_pred = model.predict(features)
    print(classification_report(labels, y_pred))

if __name__ == "__main__":
    features = np.load('data/features.npy')
    labels = np.load('data/labels.npy')
    evaluate_model('models/svm_model.pkl', features, labels)
