
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


# Testing program
if __name__ == "__main__":
    book1 = Book("Book1", "Author1", "Publisher1", 600, True)

    print("Book Title: ", book1.get_item_name())
    print("Book Author: ", book1.get_author())
    print("Book Publisher: ", book1.get_publisher())
    print("Number of Pages: ", book1.get_number_of_pages())
    print("Has eBook Version: ", "Yes" if book1.has_ebook_version() else "No")

