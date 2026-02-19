class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age) #example of init method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)
print(p1.name)
print(p1.age) #example 1


class Animal:
    def __init__(self, kind, legs):
        self.kind = kind
        self.legs = legs

a1 = Animal("Dog", 4)
print(a1.kind)
print(a1.legs) #example 2


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c1 = Car("BMW", 2020)
print(c1.brand)
print(c1.year) #example 3


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

b1 = Book("Python Basics", 300)
print(b1.title)
print(b1.pages) #example 4


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

city1 = City("Paris", 2148000)
print(city1.name)
print(city1.population) #example 5

class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age) #example of creating class without init

class Animal:
    pass

a1 = Animal()
a1.kind = "Dog"
a1.legs = 4

print(a1.kind)
print(a1.legs) #example 1


class Car:
    pass

c1 = Car()
c1.brand = "BMW"
c1.year = 2020

print(c1.brand)
print(c1.year) #example 2


class Student:
    pass

s1 = Student()
s1.name = "Alice"
s1.grade = "A"

print(s1.name)
print(s1.grade) #example 3


class Book:
    pass

b1 = Book()
b1.title = "Python Basics"
b1.pages = 300

print(b1.title)
print(b1.pages) #example 4


class City:
    pass

city1 = City()
city1.name = "Paris"
city1.population = 2148000

print(city1.name)
print(city1.population) #example 5

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age) #example of creating classes with init

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Linus", 28)
print(p1.name)
print(p1.age) #example 1


class Animal:
    def __init__(self, kind, legs):
        self.kind = kind
        self.legs = legs

a1 = Animal("Cat", 4)
print(a1.kind)
print(a1.legs) #example 2


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c1 = Car("Audi", 2022)
print(c1.brand)
print(c1.year) #example 3


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

b1 = Book("Data Science Handbook", 500)
print(b1.title)
print(b1.pages) #example 4


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

city1 = City("Berlin", 3769000)
print(city1.name)
print(city1.population) #example 5

class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age) #example of Default Values in __init__()

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)
print(p1.name, p1.age)
print(p2.name, p2.age) #example 1


class Animal:
    def __init__(self, kind, legs=4):
        self.kind = kind
        self.legs = legs

a1 = Animal("Dog")
a2 = Animal("Spider", 8)
print(a1.kind, a1.legs)
print(a2.kind, a2.legs) #example 2


class Car:
    def __init__(self, brand, year=2020):
        self.brand = brand
        self.year = year

c1 = Car("BMW")
c2 = Car("Audi", 2022)
print(c1.brand, c1.year)
print(c2.brand, c2.year) #example 3


class Book:
    def __init__(self, title, pages=100):
        self.title = title
        self.pages = pages

b1 = Book("Python Basics")
b2 = Book("Data Science Handbook", 500)
print(b1.title, b1.pages)
print(b2.title, b2.pages) #example 4


class City:
    def __init__(self, name, population=100000):
        self.name = name
        self.population = population

city1 = City("Paris")
city2 = City("Berlin", 3769000)
print(city1.name, city1.population)
print(city2.name, city2.population) #example 5

class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country) #example of Multiple Parameters and init

class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country) #example 1


class Animal:
    def __init__(self, kind, legs, habitat, continent):
        self.kind = kind
        self.legs = legs
        self.habitat = habitat
        self.continent = continent

a1 = Animal("Tiger", 4, "Jungle", "Asia")
print(a1.kind)
print(a1.legs)
print(a1.habitat)
print(a1.continent) #example 2


class Car:
    def __init__(self, brand, year, color, country):
        self.brand = brand
        self.year = year
        self.color = color
        self.country = country

c1 = Car("Tesla", 2023, "Red", "USA")
print(c1.brand)
print(c1.year)
print(c1.color)
print(c1.country) #example 3


class Book:
    def __init__(self, title, pages, author, language):
        self.title = title
        self.pages = pages
        self.author = author
        self.language = language

b1 = Book("Python Handbook", 450, "John Smith", "English")
print(b1.title)
print(b1.pages)
print(b1.author)
print(b1.language) #example 4


class City:
    def __init__(self, name, population, country, region):
        self.name = name
        self.population = population
        self.country = country
        self.region = region

city1 = City("Berlin", 3769000, "Germany", "Europe")
print(city1.name)
print(city1.population)
print(city1.country)
print(city1.region) #exaple 5