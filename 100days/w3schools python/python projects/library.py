class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")

    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book} removed form the library'")

        else:
            print(f"Book '{book} not found in the library'")

    def display_book(self):
        if self.books:
            print(f"Book in the library: {', '.join(self.books)}")
        else:
            print("The library is empty.")



# Crearrte a Library objects
my_library = Library("My Library")

# Add books to the library

my_library.add_book("Muna Madan ")
my_library.add_book("Seto Darti")
my_library.add_book("Paralko Ago")
my_library.add_book("Chin Yatra")

# Remove books from the library 
my_library.remove_book("Paralko Ago")
my_library.remove_book("sereofero")


# Display the upadated list of books 

my_library.display_book()


