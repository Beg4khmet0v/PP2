def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") #example of passing different arguments to the same function from w3schools.com

def greet(name):
    print("Hello, " + name + ". How are you?")
greet("Alice")
greet("Bob") #example 1

def sum_two_numbers(a, b):
    return a + b
result1 = sum_two_numbers(3, 5)
result2 = sum_two_numbers(10, 20) #example 2

def calculate_area_of_circle(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area
radius1 = 5
radius2 = 10
area1 = calculate_area_of_circle(radius1)
area2 = calculate_area_of_circle(radius2) #example 3

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(4)) #example 4

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) #example 5
    
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument, which is passed to the function when it is called from w3schools.com   

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") #example of calling a function with right number of arguments from w3schools.com

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil") #example of mistake of calling a function with missing arguments from w3schools.com

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus") #example of using default parameter value in a function from w3schools.com

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") #another one example of using default parameter value in a function from w3schools.com

def my_function(food = "Pizza"):
  print("I like", food)

my_function("Sushi")
my_function() #example 1


def my_function(height = "tall"):
  print("I am", height) 

my_function("short")
my_function() #example 2


def my_function(language = "Python"):
    print("I love", language)
my_function("JavaScript")
my_function() #example 3


def my_function(color = "blue"):
    print("My favorite color is", color)
my_function("red")
my_function() #example 4


def my_function(car = "Toyota"):
    print("I drive a", car)
my_function("Honda")
my_function() #example 5

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy") #example of using keyword arguments to call a function from w3schools.com

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog") #example of using keyword arguments in different order to call a function from w3schools.com

def my_function(food, drink):
  print("I like", food)
  print("I also like", drink)
my_function(drink = "coffee", food = "pasta") #example 1

def my_function(city, country):
  print("I live in", city)
  print("I am from", country)
my_function(country = "USA", city = "New York") #example 2

def my_function(name, age):
  print("My name is", name)
  print("I am", age, "years old")
my_function(age = 30, name = "Alice") #example 3

def my_function(hobby, sport):
  print("My hobby is", hobby)
  print("My favorite sport is", sport)
my_function(sport = "soccer", hobby = "painting") #example 4

def my_function(movie, music):
  print("My favorite movie is", movie)
  print("My favorite music genre is", music)
my_function(music = "rock", movie = "Inception") #example 5

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy") #example of calling a function with positional arguments from w3schools.com

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog") #example of mistake of calling a function with positional arguments in wrong order from w3schools.com

def my_function(food, drink):
  print("I like", food)
  print("I also like", drink)
my_function("pasta", "coffee") #example 1

def my_function(city, country):
  print("I live in", city)
  print("I am from", country)
my_function("New York", "USA") #example 2

def my_function(name, age):
  print("My name is", name)
  print("I am", age, "years old")
my_function("Alice", 30) #example 3

def my_function(hobby, sport):
  print("My hobby is", hobby)
  print("My favorite sport is", sport)
my_function("painting", "soccer") #example 4

def my_function(movie, music):
  print("My favorite movie is", movie)
  print("My favorite music genre is", music)
my_function("Inception", "rock") #example 5

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5) #example of mixing positional and keyword arguments in a function call from w3schools.com

def my_function(name, age, city):
  print("My name is", name)
  print("I am", age, "years old")
  print("I live in", city)
my_function("Alice", city = "New York", age = 30) #example 1

def my_function(hobby, sport, music):
  print("My hobby is", hobby)
  print("My favorite sport is", sport)
  print("My favorite music genre is", music)
my_function("painting", music = "rock", sport = "soccer") #example 2

def my_function(movie, music, food):
  print("My favorite movie is", movie)
  print("My favorite music genre is", music)
  print("My favorite food is", food)
my_function("Inception", food = "pizza", music = "rock") #example 3

def my_function(city, country, language):
  print("I live in", city)
  print("I am from", country)
  print("I speak", language)
my_function("New York", language = "English", country = "USA") #example 4

def my_function(name, age, hobby):
  print("My name is", name)
  print("I am", age, "years old")
  print("My hobby is", hobby)
my_function("Alice", hobby = "painting", age = 30) #example 5

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits) #example of passing a list as an argument to a function from w3schools.com

def my_function(vehicles):
  for vehicle in vehicles:
    print(vehicle)
my_vehicles = ["car", "bike", "bus"]
my_function(my_vehicles) #example 1

def my_function(colors):
  for color in colors:
    print(color)
my_colors = ["red", "green", "blue"]
my_function(my_colors) #example 2

def my_function(countries):
  for country in countries:
    print(country)
my_countries = ["USA", "Canada", "Mexico"]
my_function(my_countries) #example 3

def my_function(languages):
  for language in languages:
    print(language)
my_languages = ["Python", "JavaScript", "Java"]
my_function(my_languages) #example 4

def my_function(hobbies):
  for hobby in hobbies:
    print(hobby)
my_hobbies = ["painting", "soccer", "cooking"]
my_function(my_hobbies) #example 5

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person) #example of passing a dictionary as an argument to a function from w3schools.com

def my_function(book):
  print("Title:", book["title"])
  print("Author:", book["author"])
my_book = {"title": "To Kill a Mockingbird", "author": "Harper Lee"}
my_function(my_book) #example 1

def my_function(movie):
  print("Title:", movie["title"])
  print("Director:", movie["director"])
my_movie = {"title": "Inception", "director": "Christopher Nolan"}
my_function(my_movie) #example 2

def my_function(car):
  print("Make:", car["make"])
  print("Model:", car["model"])
my_car = {"make": "Toyota", "model": "Camry"}
my_function(my_car) #example 3

def my_function(student):
  print("Name:", student["name"])
  print("Grade:", student["grade"])
my_student = {"name": "Alice", "grade": "A"}
my_function(my_student) #example 4

def my_function(city):
  print("City:", city["name"])
  print("Population:", city["population"])
my_city = {"name": "New York", "population": 8000000}
my_function(my_city) #example 5

def my_function(name, /):
  print("Hello", name)

my_function("Emil") #example of using a positional-only parameter in a function from w3schools.com

def my_function(name):
  print("Hello", name)

my_function(name = "Emil") #same example but without ,/ in the function definition, which allows for keyword arguments from w3schools.com

def my_function(name, /):
  print("Hello", name)

my_function(name = "Emil") #example of mistake of using a keyword argument with a positional-only parameter in a function from w3schools.com

def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil") #example of using a keyword-only parameter in a function from w3schools.com

def my_function(name):
  print("Hello", name)

my_function("Emil") #same example but without *, which allows for positional arguments from w3schools.com

def my_function(*, name):
  print("Hello", name)

my_function("Emil") #example of mistake of using a positional argument with a keyword-only parameter in a function from w3schools.com

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result) #example of using a function with both positional-only and keyword-only parameters from w3schools.com