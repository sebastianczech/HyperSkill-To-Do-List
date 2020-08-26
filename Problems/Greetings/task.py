class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, I am {}!".format(self.name)

    # create the method greet here


person = Person(input())
print(person.greet())
