import argparse
import os
import numpy as np

# Import the modules
from src.preprocess import preprocess_images
from src.feature_extraction import extract_hog_features
from src.train import train_svm
from src.evaluate import evaluate_model
from src.predict import predict_pose

def main(args):
    if args.preprocess:
        print("Preprocessing images...")
        preprocess_images('data/raw', 'data/processed')
        print("Preprocessing completed.")
    
    if args.feature_extraction:
        print("Extracting features...")
        features, labels = extract_hog_features('data/processed')
        np.save('data/features.npy', features)
        np.save('data/labels.npy', labels)
        print("Feature extraction completed.")
    
    if args.train:
        print("Training model...")
        features = np.load('data/features.npy')
        labels = np.load('data/labels.npy')
        model = train_svm(features, labels)
        import joblib
        joblib.dump(model, 'models/svm_model.pkl')
        print("Model training completed.")
    
    if args.evaluate:
        print("Evaluating model...")
        features = np.load('data/features.npy')
        labels = np.load('data/labels.npy')
        evaluate_model('models/svm_model.pkl', features, labels)
        print("Model evaluation completed.")
    
    if args.predict:
        print("Predicting pose...")
        pose = predict_pose('models/svm_model.pkl', args.image_path)
        print(f"Predicted Pose: {pose}")

if __name__ == "_main_":
    parser = argparse.ArgumentParser(description="Bharatanatyam Pose Detection")
    
    parser.add_argument('--preprocess', action='store_true', help='Preprocess images')
    parser.add_argument('--feature_extraction', action='store_true', help='Extract features')
    parser.add_argument('--train', action='store_true', help='Train model')
    parser.add_argument('--evaluate', action='store_true', help='Evaluate model')
    parser.add_argument('--predict', action='store_true', help='Predict pose')
    parser.add_argument('--image_path', type=str, help='Path to the image for prediction')

    args = parser.parse_args()
    main(args)