""" The module """

import pickle

class CustomObject:
    """ Custom object? """

    def __init__(self, name='', age=0, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")
    
    def serialize(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, filename)
    
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename) as file:
                data = pickle.load(file)
                return data
        except:
            return None
