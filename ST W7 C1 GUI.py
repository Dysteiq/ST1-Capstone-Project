import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def write_to_file(words):
    try:
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if filename:
            with open(filename, "w") as file:
                for word in words:
                    file.write(word + "\n")
    except Exception as e:
        messagebox.showerror(str(e), "Failed to write to file")


root = tk.Tk()
root.title("Word Writer")

num_words_label = tk.Label(root, text="Enter the number of words:")
num_words_label.pack()
num_words_entry = tk.Entry(root)
num_words_entry.pack()


def ask_number_of_words():
    num_words = int(num_words_entry.get())
    word_input_frame.pack_forget()  # Hide the input elements
    input_words(num_words)


start_button = tk.Button(root, text="Start", command=ask_number_of_words)
start_button.pack()

word_input_frame = tk.Frame(root)


def input_words(num_words):
    words = []

    def add_word():
        word_label_text = f"Enter word {len(words) + 2}:"
        word_label.config(text=word_label_text)
        word = word_entry.get()
        words.append(word)
        word_entry.delete(0, "end")
        if len(words) == num_words:
            write_to_file(words)
            root.destroy()

    word_label = tk.Label(word_input_frame, text=f"Enter word 1:")
    word_label.pack()
    word_entry = tk.Entry(word_input_frame)
    word_entry.pack()
    add_button = tk.Button(word_input_frame, text="Add word", command=add_word)
    add_button.pack()

    if len(words) < num_words:
        word_input_frame.pack()
    else:
        write_to_file(words)
        root.destroy()


root.mainloop()
