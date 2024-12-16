# Define a class
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet(self):  # Method
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create an object
person1 = Person("Alice", 25)
print(person1.greet())  # Output: Hello, my name is Alice and I am 25 years old.
