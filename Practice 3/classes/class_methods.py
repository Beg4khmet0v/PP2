class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet() #example of creating the method in a class

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet() #Example 1


class Animal:
    def __init__(self, kind):
        self.kind = kind

    def sound(self):
        print("The " + self.kind + " makes a sound")

a1 = Animal("Dog")
a1.sound()  #example 2


class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print("Driving a " + self.brand)

c1 = Car("Tesla")
c1.drive() # example 3


class Book:
    def __init__(self, title):
        self.title = title

    def read(self):
        print("Reading " + self.title)

b1 = Book("Python Basics")
b1.read() #example 4


class City:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print("Welcome to " + self.name)

city1 = City("Paris")
city1.describe() #example 5

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7)) #example of Creating a method with parameters

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7)) #example 1


class Animal:
    def speak(self, sound, times):
        return (sound + " ") * times

a1 = Animal()
print(a1.speak("Woof", 3)) #example 2


class Car:
    def drive(self, brand, speed):
        return f"Driving {brand} at {speed} km/h"

c1 = Car()
print(c1.drive("Tesla", 120)) #example 3


class Student:
    def study(self, subject, hours):
        return f"Studying {subject} for {hours} hours"

s1 = Student()
print(s1.study("Math", 2)) #example 4


class Book:
    def read(self, title, pages):
        return f"Reading {title}, {pages} pages"

b1 = Book()
print(b1.read("Python Basics", 300)) #example 5

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info()) #example of method that accesses object properties

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info()) #example 1


class Animal:
    def __init__(self, kind, legs):
        self.kind = kind
        self.legs = legs

    def get_info(self):
        return f"{self.kind} has {self.legs} legs"

a1 = Animal("Dog", 4)
print(a1.get_info()) #example 2


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_info(self):
        return f"{self.brand} was made in {self.year}"

c1 = Car("Tesla", 2023)
print(c1.get_info()) #example 3


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def get_info(self):
        return f"{self.title} has {self.pages} pages"

b1 = Book("Python Basics", 300)
print(b1.get_info()) #example 4

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def get_info(self):
        return f"{self.name} has a population of {self.population}"

city1 = City("Paris", 2148000)
print(city1.get_info()) #example 5

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1 
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()#example of method that changes a property value

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday() #example 1


class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1
        print(f"Counter is now {self.value}")

c1 = Counter()
c1.increment()
c1.increment() #example 2


class BankAccount:
    def __init__(self, balance=100):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance is now {self.balance}")

acc1 = BankAccount()
acc1.deposit(50)
acc1.deposit(25) #example 3


class Light:
    def __init__(self, state="off"):
        self.state = state

    def switch(self):
        self.state = "on" if self.state == "off" else "off"
        print(f"Light is now {self.state}")

lamp = Light()
lamp.switch()
lamp.switch() #example 4


class Score:
    def __init__(self, points=0):
        self.points = points

    def add_points(self, value):
        self.points += value
        print(f"Score is now {self.points}")

s1 = Score()
s1.add_points(10)
s1.add_points(20)  #example 5

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1) #example without str method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)
print(p1) #example 1


class Animal:
    def __init__(self, kind, legs):
        self.kind = kind
        self.legs = legs

a1 = Animal("Dog", 4)
print(a1) #example 2


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c1 = Car("Tesla", 2023)
print(c1) #example 3


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

b1 = Book("Python Basics", 300)
print(b1) #example 4


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

city1 = City("Paris", 2148000)
print(city1) #example 5

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})" 

p1 = Person("Tobias", 36)
print(p1) #example with str method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1) #example 1 


class Animal:
    def __init__(self, kind, legs):
        self.kind = kind
        self.legs = legs

    def __str__(self):
        return f"{self.kind} with {self.legs} legs"

a1 = Animal("Dog", 4)
print(a1) #example 2


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"{self.brand} ({self.year})"

c1 = Car("Tesla", 2023)
print(c1) #example 3


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' - {self.pages} pages"

b1 = Book("Python Basics", 300)
print(b1) #example 4


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f"{self.name}, population {self.population}"

city1 = City("Paris", 2148000)
print(city1) #example 5

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs() # example that Create multiple methods in a class

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")

    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs() #example 1


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")

acc = BankAccount("Alice")
acc.deposit(100)
acc.withdraw(40)
acc.show_balance() #example 2


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book}")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed book: {book}")

    def show_books(self):
        print(f"Library '{self.name}':")
        for book in self.books:
            print(f"- {book}")

lib = Library("Central Library")
lib.add_book("1984")
lib.add_book("Brave New World")
lib.show_books() #example 3


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added item: {item}")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed item: {item}")

    def show_cart(self):
        print("Shopping Cart:")
        for item in self.items:
            print(f"- {item}")

cart = ShoppingCart()
cart.add_item("Milk")
cart.add_item("Bread")
cart.show_cart() #example 4


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)
        print(f"Added player: {player}")

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            print(f"Removed player: {player}")

    def show_team(self):
        print(f"Team '{self.name}':")
        for player in self.players:
            print(f"- {player}")

team = Team("Warriors")
team.add_player("John")
team.add_player("Mike")
team.show_team() #example 5


class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")

del Person.greet

p1.greet() # This will cause an error, example, I guess, no needs to make examples with errors ))

