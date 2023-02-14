class MyString:
    def __init__(self):
        self.my_string = ""

    def getString(self):
        self.my_string = input("Enter a string: ")

    def printString(self):
        print(self.my_string.upper())

s = MyString()
s.getString()
s.printString()