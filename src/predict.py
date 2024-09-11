import cv2
import joblib
import numpy as np
from skimage.feature import hog
import tkinter as tk
from tkinter import filedialog, messagebox

def preprocess_image(img_path, img_size=(128, 128)):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, img_size)
    return img

def extract_hog_feature(img):
    hog_feature = hog(img, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=False)
    return hog_feature.reshape(1, -1)

def predict_pose(model_path, img_path):
    model = joblib.load(model_path)
    img = preprocess_image(img_path)
    feature = extract_hog_feature(img)
    prediction = model.predict(feature)
    return prediction[0]

def select_image():
    img_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if img_path:
        try:
            pose = predict_pose(model_path, img_path)
            result_label.config(text=f"Predicted Pose: {pose}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    model_path = 'models/svm_model.pkl'

    # Set up the Tkinter window
    root = tk.Tk()
    root.title("Pose Prediction")

    # Create a button to select an image
    select_button = tk.Button(root, text="Select Image", command=select_image)
    select_button.pack(pady=20)

    # Create a label to display the prediction result
    result_label = tk.Label(root, text="Predicted Pose: None", font=("Helvetica", 14))
    result_label.pack(pady=20)

    # Run the Tkinter event loop
    root.mainloop()
