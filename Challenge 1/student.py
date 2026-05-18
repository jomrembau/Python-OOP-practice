import random

class Student:

    def __init__(self, name, age, educational_platform = "Udemy"):
        self.name = name
        self.age = age
        self.educational_platform = educational_platform

    def greet(self):
        greetings = ["Hi, I'm ", "Hey there, My name is ", "Hello. My name is "]
        return random.choice(greetings)
