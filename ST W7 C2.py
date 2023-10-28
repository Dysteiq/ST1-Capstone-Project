import os
import tkinter as tk
from tkinter import filedialog

average_length = 0

root = tk.Tk()

label = tk.Label(root, text=f"Average word length: {average_length:.2f}")
label.pack()

file_path = filedialog.askopenfilename(title="Select a File")


def read_file():
    with open(file_path, "r") as file:
        file_content = file.read()

    words = file_content.split()
    total_length = sum(len(word) for word in words)
    num_words = len(words)

    if num_words > 0:
        average_length = total_length / num_words
        label.config(text=f"Average word length: {average_length:.2f}")


if __name__ == "__main__":
    read_file()

root.mainloop()

