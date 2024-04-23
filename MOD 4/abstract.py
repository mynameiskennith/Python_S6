# A class which contains one or more abstract methods is called abstract class
# abstract method is a method that has a declaration but does not have an implementation
# by default python does not contain abstract class. But a module ABC provides abstraction

from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    def __init__(self):
        self.sides = 3

    def noofsides(self):
        print('I have 3 sides')

class Pentagon(Polygon):
    def noofsides(self):
        print('I have 5 sides')

R = Triangle()
R.noofsides()
Pentagon().noofsides()
