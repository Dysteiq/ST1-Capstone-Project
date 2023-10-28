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


class Book(LibraryItem):
    def __init__(self, item_name, author, publisher, number_of_pages, has_ebook):
        super().__init__(item_name, author, publisher)
        self.number_of_pages = number_of_pages
        self.has_ebook = has_ebook

    # Accessors
    def get_number_of_pages(self):
        return self.number_of_pages

    def has_ebook_version(self):
        return self.has_ebook

    # Mutators
    def set_number_of_pages(self, number_of_pages):
        self.number_of_pages = number_of_pages

    def set_ebook_version(self, has_ebook):
        self.has_ebook = has_ebook


def display_selected_item():
    item = combobox.get()
    item_dict = {
        "Book 1": book1,
        "Book 2": book2,
        "Book 3": book3,
    }
    item = item_dict[item]
    text = (f"Item Name: {item.get_item_name()}\nAuthor: {item.get_author()}\nPublisher: {item.get_publisher()}\n"
            f"Page Count:{item.get_number_of_pages()}\n Has eBook?: {'Yes' if item.has_ebook_version() else 'No'}")
    txt_answer.delete(1.0, "end")
    txt_answer.insert(1.0, text)


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Library Book")

    if __name__ == "__main__":
        book1 = Book("Book1", "Author1", "Publisher1", 500, False)
        book2 = Book("Book2", "Author2", "Publisher2", 350, True)
        book3 = Book("Book3", "Author3", "Publisher3", 400, True)

        combobox = ttk.Combobox(root, values=["Book 1", "Book 2", "Book 3"])
        combobox.pack()

        button = tk.Button(root, text="Display Information", command=display_selected_item)
        button.pack()

        txt_answer = tk.Text(root, bg="#c6eafa", width=40, height=10)
        txt_answer.pack()

        root.mainloop()
