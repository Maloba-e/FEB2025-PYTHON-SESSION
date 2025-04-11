### Encapsulation ###
class Book:
    def __init__(self,title,author,year): #initialization
        self.title=title
        self.author=author
        self.year=year
        self.available=True #default to available
        
    def borrow(self):
        """
        marks the book borrowed if available
        """
        if self.available:
            self.available= False
            return f"you have borrowed `{self.title}`."
        else:
            return f"Sorry, {self.title} is not available."
        
    def rtn_book(self):
        """
        Marks the book as returned
        """
        self.available=True
        return f"you have returned {self.title}."
    
    def get_details(self):
        '''
        returns formatted book information
        '''
        return f"Title: {self.title} by Author: {self.author} of Year: {self.year}"
            
            
# Book.get_details()
# Book.available =            
# Book.get_details()
