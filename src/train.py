# src/train.py
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_svm(features, labels):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    clf = svm.SVC(kernel='linear')
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    return clf

if __name__ == "__main__":
    features = np.load('data/features.npy')
    labels = np.load('data/labels.npy')
    model = train_svm(features, labels)
    import joblib
    joblib.dump(model, 'models/svm_model.pkl')
