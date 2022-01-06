"""
Python Decorater
"""


class Undecorated:
    @staticmethod
    def get():
        return "Undecorated object"


class Decorated:
    def __init__(self, un_decorated):
        self.un_decorated = un_decorated

    def get(self):
        return self.un_decorated.get().replace("Undecorated", "Decorated")


undecorated = Undecorated()
print(undecorated.get())

decorated = Decorated(undecorated)
print(decorated.get())
#Here bcoz u are passing the object of above class at the time of below class instantiation
