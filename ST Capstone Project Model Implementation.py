# GUI

import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Paths and Model Name
model_name = 'my_model.h5'
model_dir = 'E:/Stuff/University/Assignments/Software Technology/ST Capstone Project/'
model_path = os.path.join(model_dir, model_name)

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)


def load_existing_model():
    try:
        loaded_model = load_model(model_path)
        print("Model successfully loaded")
    except FileNotFoundError:
        return None
    return loaded_model


model = load_existing_model()


def display_image(file_path):
    image = Image.open(file_path)
    displayed_image = ImageTk.PhotoImage(image)  # Create a PhotoImage object from the PIL image
    canvas.create_image(0, 0, image=displayed_image, anchor=tk.NW)


def preprocess_image(file_path):
    image = load_img(file_path, target_size=(128, 128))
    image = img_to_array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image


def predict_image(file_path):
    preprocessed_image = preprocess_image(file_path)
    prediction = model.predict(preprocessed_image)
    print(prediction)
    try:
        if prediction[0][0] > 0.45:
            result = "Lion"
        else:
            result = "Cheetah"
        messagebox.showinfo("Prediction", f"The image is classified as a {result}")
    except ValueError:
        messagebox.showerror("Prediction Error", "Failed to make a prediction.")


def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        display_image(file_path)
        predict_image(file_path)


def exit_program():
    root.destroy()


def main():
    btn_browse = Button(root, text="Browse", command=load_image, bg="#cc7aff")
    btn_exit = Button(root, text="Exit", command=exit_program, bg="#cc7aff")

    if model is None:
        messagebox.showerror("FileNotFoundError", "Could not find saved model")

    root.title("Lion or Cheetah Image Classification Tool")
    root.configure(bg="#ebebeb")
    btn_browse.grid(row=5, column=1, padx=5, pady=5)
    btn_exit.grid(row=5, column=3, padx=5, pady=5)

    canvas.grid(row=1, column=1, columnspan=3)

    root.mainloop()  # Main GUI loop


if __name__ == "__main__":
    main()
