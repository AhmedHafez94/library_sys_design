from curses.ascii import isdigit
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
        self.users_lst = []
        self.search_dic = {} # key name prefix value will be [book] 


    def add_book(self, book: Book):
        self.books_lst.append(book) 
        self.add_book_to_search_dic(book)


    def print_library_books(self):
        for book in self.books_lst:
            print(str(book))   


    def add_book_to_search_dic(self, book: Book):
        book_name = book.name 
        book_char = "" 
        for letter in book_name:
            book_char += letter 
            self.search_dic.setdefault(book_char, [])  
            self.search_dic[book_char].append(book)        

    def search_library_books(self, search_word):
        print("search_library_books called ") 
        search_result = self.search_dic.get(search_word, [])
        if len(search_result) > 0 :
            for book in search_result:
                print(str(book))
        else:
            print("book does not exist")

    def add_new_user(self, user: User):
        self.users_lst.append(user) 



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
        if user_choice.isdigit():
            return int(user_choice)
        else:
            return 100
        # return int(user_choice ) 

    def run_Programme(self):
        while True:
            choice = self.print_menu_options() 

            if choice == 1:
                book_name = input("enter book name: ")
                book_id = input("enter book id: ")
                book_quantity = int(input("enter book quantity: "))
                self.libr_manager.add_book(Book(book_id, book_name, book_quantity))

            elif choice == 2:
                for book in self.libr_manager.books_lst:
                    print(str(book))

            elif choice == 3:
                print("choice is 3")
                prefix = input("enter name of the book: ")
                self.libr_manager.search_library_books(prefix)
            elif choice == 4:
                print("choice is 4")
                user_id = input("enter user id: ")
                user_name = input("enter user name: ")
                new_user = User(user_id, user_name)
                self.libr_manager.add_new_user(new_user)
                
            elif choice == 5:
                print("choice is 5")
            elif choice == 6:
                print("choice is 6")
            else:
                print("choice does not exist")



xz = Library_Front_End()
xz.run_Programme()      