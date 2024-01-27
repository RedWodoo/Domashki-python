"""
program
"""
class Book():
    """
    program
    """
    def __init__(self,name,publish,publisher,genre_book,author,price):
        """
        program
        """
        self.name = name
        self.publish = publish
        self.publisher = publisher
        self.genre_book = genre_book
        self.author = author
        self.price = price
    def description(self, text):
        """
        program
        """
        return f'{self.name} --- {text}'
    def nothing(self):
        """
        program
        """
Somebook = Book('1894',2016,'WBP','multiverse',"George OrWell","20$")
print(Somebook.name)
text_input = input('Give description: ')
print(Somebook.description(text_input))
