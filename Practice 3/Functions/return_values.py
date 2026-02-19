def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message) #example of using a return value from a function from w3schools.com

def add_numbers(a, b):
    return a + b
result = add_numbers(3, 5)
print(result) #example 1

def multiply_numbers(a, b):
    return a * b
result = multiply_numbers(4, 6)
print(result) #example 2

def calculate_area_of_rectangle(length, width):
    area = length * width
    return area
length = 5
width = 3
area = calculate_area_of_rectangle(length, width)
print(area) #example 3

def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False
print(is_odd(7)) #example 4

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10)) #example 5 

def get_greeting():
  return "Hello from a function"

print(get_greeting()) #example of directly printing the return value from a function without storing it in a variable from w3schools.com

def add_numbers(a, b):
    return a + b
print(add_numbers(3, 5)) #example 1

def multiply_numbers(a, b):
    return a * b
print(multiply_numbers(4, 6)) #example 2

def calculate_area_of_rectangle(length, width):
    area = length * width
    return area
print(calculate_area_of_rectangle(5, 3)) #example 3

def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False
print(is_odd(7)) #example 4

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10)) #example 5

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2]) #example of returning a list from a function and accessing its elements from w3schools.com

def my_function():
  return ["car", "bike", "bus"]
vehicles = my_function()
print(vehicles[0])
print(vehicles[1])
print(vehicles[2]) #example 1

def my_function():
    return ["red", "green", "blue"]
colors = my_function()
print(colors[0])
print(colors[1])
print(colors[2]) #example 2

def my_function():
    return ["USA", "Canada", "Mexico"]
countries = my_function()
print(countries[0])
print(countries[1])
print(countries[2]) #example 3

def my_function():
    return ["Python", "JavaScript", "Java"]
languages = my_function()
print(languages[0])
print(languages[1])
print(languages[2]) #example 4

def my_function():
    return ["Inception", "The Matrix", "Interstellar"]
movies = my_function()
print(movies[0])
print(movies[1])
print(movies[2]) #example 5

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y) #example of a function that returns a tuple from w3schools.com

def my_function():
    return (3, 5)
a, b = my_function()
print("a:", a)
print("b:", b) #example 1

def my_function():
    return (4, 6)
x, y = my_function()
print("x:", x)
print("y:", y) #example 2

def my_function():
    return (5, 3)
length, width = my_function()
print("length:", length)
print("width:", width) #example 3

def my_function():
    return (7, 9)
num1, num2 = my_function()
print("num1:", num1)
print("num2:", num2) #example 4

def my_function():
    return (10, 20)
a, b = my_function()
print("a:", a)
print("b:", b) #example 5   