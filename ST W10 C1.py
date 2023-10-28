import tkinter as tk
from tkinter import ttk

class LibraryItem:
    def __init__ (self, item_name, author, publisher):
        self.item_name = item_name
        self.author = author
        self.publisher = publisher

    # Accessors
    def get_item_name(self):
        return self.item_name

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    # Mutators
    def set_item_name(self, item_name):
        self.item_name = item_name

    def set_author(self, author):
        self.author = author

    def set_publisher(self, publisher):
        self.publisher = publisher


def display_selected_item():
    item = combobox.get()
    item_dict = {
        "Item 1": item1,
        "Item 2": item2,
        "Item 3": item3,
    }
    item = item_dict[item]
    text = f"Item Name: {item.get_item_name()}\nAuthor: {item.get_author()}\nPublisher: {item.get_publisher()}"
    txt_answer.delete(1.0, "end")
    txt_answer.insert(1.0, text)


root = tk.Tk()
root.title("Library Item")

if __name__ == "__main__":
    item1 = LibraryItem("Book1", "Author1", "Publisher1")
    item2 = LibraryItem("Book2", "Author2", "Publisher2")
    item3 = LibraryItem("Book3", "Author3", "Publisher3")

    combobox = ttk.Combobox(root, values=["Item 1", "Item 2", "Item 3"])
    combobox.pack()

    button = tk.Button(root, text="Display Information", command=display_selected_item)
    button.pack()

    txt_answer = tk.Text(root, bg="#c6eafa", width=40, height=10)
    txt_answer.pack()

    root.mainloop()



