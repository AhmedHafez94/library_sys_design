from mimetypes import init


print("Hello world")

class Book:
    def __init__(self, id, name, quantity):
        self.id = id 
        self.name = name 
        self.quantity = quantity 

    def __str__(self):
        return f'Book name: {self.name} id {self.id} and quantity {self.quantity}'

class User:
    def __init__(self,id, name) -> None:
        self.id = id 
        self.name = name 



class LibraryManager: 
    def __init__(self) -> None:
        self.books_lst = [] 


    def add_book(self, book: Book):
        self.books_lst.append(book) 

    def print_library_books(self):
        for book in self.books_lst:
            print(str(book))    
        

class Library_Front_End():
    def __init__(self) -> None:
        self.libr_manager = LibraryManager()

    def print_menu_options(self):
        print("Program Options: ") 
        options = [
                "add book", 
                "print library books",
                "print books by prefix",
                "add user",
                "borrow book",
                "return book",
                "print users borrowed book",
                "print users"
              ]

        options = [f'{idx + 1}: {option}' for idx, option in enumerate(options)] 
        print("\n".join(options)) 
        user_choice = input("enter your option: ") 

        return int(user_choice )

    def run_Programme(self):
        while True:
            choice = self.print_menu_options() 

            if choice == 1:
                book_name = input("enter book name: ")
                book_id = input("enter book id: ")
                book_quantity = int(input("enter book quantity: "))
                self.libr_manager.add_book(Book(book_id, book_name, book_quantity))

xz = Library_Front_End()
xz.print_menu_options()        