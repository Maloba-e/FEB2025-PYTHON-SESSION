from book import Book

class DigitalBook(Book):
    def __init__(self, title, author, year, file_size):
        #using super() to inherit attributes from the Book class
        super().__init__(title, author, year)
        self.file_size = file_size
        
    def stream(self):
            #streaming the book content
        return f"Streaming {self.title} - size:{self.file_size}MB"
    
    def borrow(self):
        #borrowing the book
        return f"{self.title} just stream"