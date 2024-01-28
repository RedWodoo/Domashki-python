"""
program
"""
class Main():
    """
    program
    """
    def __init__(self,text) -> None:
        """
        program
        """
        self.text = text
    def method1(self,text):
        """
        program
        """
        self.text = text
    def nothing(self):
        """
        program
        """
    class Child():
        """
        program
        """
        number = 3.14
        def __init__(self,name,number) -> None:
            """
            program
            """
            self.name = name
            self.number = number
        def nothing(self):
            """
            program
            """
        def nothing2(self):
            """
            program
            """
text1 = Main("Some text")
number1 = Main.Child('PI number is',Main.Child.number)
print(text1.text)
print(number1.name,number1.number)
