
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


# Testing program
if __name__ == "__main__":
    item1 = LibraryItem("Book1", "Author1", "Publisher1")
    item2 = LibraryItem("Book2", "Author2", "Publisher2")
    item3 = LibraryItem("Book3", "Author3", "Publisher3")

    print("Item 1 - Name: {}, Author: {}, Publisher: {}".format(item1.get_item_name(), item1.get_author(),
                                                                item1.get_publisher()))
    print("Item 2 - Name: {}, Author: {}, Publisher: {}".format(item2.get_item_name(), item2.get_author(),
                                                                item2.get_publisher()))
    print("Item 3 - Name: {}, Author: {}, Publisher: {}".format(item3.get_item_name(), item3.get_author(),
                                                                item3.get_publisher()))
