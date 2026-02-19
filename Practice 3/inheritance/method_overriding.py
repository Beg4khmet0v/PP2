class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) #example from w3schools


class Animal:
    def sound(self):
        print("Animal makes a sound")

class Cat(Animal):
    def sound(self):
        print("Cat says meow")

c = Cat()
c.sound()  # example 1


class Shape:
    def area(self):
        print("Area not defined")

class Circle(Shape):
    def area(self):
        print("Area = πr²")

circle = Circle()
circle.area()  # example 2


class Employee:
    def salary(self):
        print("Base salary")

class Manager(Employee):
    def salary(self):
        print("Salary + Bonus")

m = Manager()
m.salary()  # example 3


class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car engine started")

car = Car()
car.start()  # example 4


class Person2:
    def introduce(self):
        print("I am a person")

class Student2(Person2):
    def introduce(self):
        print("I am a student")

s = Student2()
s.introduce()  # example 5