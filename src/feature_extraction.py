# src/feature_extraction.py
import cv2
import os
import numpy as np
from skimage.feature import hog

def extract_hog_features(image_dir):
    features = []
    labels = []
    for pose in os.listdir(image_dir):
        pose_dir = os.path.join(image_dir, pose)
        for img_name in os.listdir(pose_dir):
            img_path = os.path.join(pose_dir, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            hog_feature = hog(img, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=False)
            features.append(hog_feature)
            labels.append(pose)
    return np.array(features), np.array(labels)

if __name__ == "__main__":
    features, labels = extract_hog_features('data/processed')
    np.save('data/features.npy', features)
    np.save('data/labels.npy', labels)
