# src/preprocess.py
import cv2
import os

def preprocess_images(input_dir, output_dir, img_size=(128, 128)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for pose in os.listdir(input_dir):
        pose_dir = os.path.join(input_dir, pose)
        output_pose_dir = os.path.join(output_dir, pose)
        if not os.path.exists(output_pose_dir):
            os.makedirs(output_pose_dir)

        for img_name in os.listdir(pose_dir):
            img_path = os.path.join(pose_dir, img_name)
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
            img = cv2.resize(img, img_size)  # Resize image
            cv2.imwrite(os.path.join(output_pose_dir, img_name), img)

if __name__ == "__main__":
    preprocess_images('data/raw', 'data/processed')
