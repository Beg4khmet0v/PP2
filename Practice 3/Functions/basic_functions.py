def my_function():
  print("Hello from a function") 

my_function() #example of a basic function from w3schools.com with calling the function

def greet(name):
    print("Hello, " + name + ". How are you?")

greet("Alice") #example 1

def sum_two_numbers(a, b):
  return a + b
sum_two_numbers(3, 5) #example 2

def calculate_area_of_circle(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area
radius = 5
area = calculate_area_of_circle(radius) #example 3

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
        return n * factorial(n - 1)
print(factorial(5)) #example 5

def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function() #example of calling the same function multiple times from w3schools.com

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
print(is_even(4))
print(is_even(7)) #example 4

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
print(factorial(0)) #example 5  

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3) #example of solving problems without using functions from w3schools.com

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50)) #example of solving same problems using functions from w3schools.com

speed1 = 60
time1 = 2
distance1 = speed1 * time1
print(distance1)

speed2 = 80
time2 = 3
distance2 = speed2 * time2
print(distance2)

speed3 = 100
time3 = 1.5
distance3 = speed3 * time3
print(distance3) #example 1

def calculate_distance(speed, time):
    return speed * time
print(calculate_distance(60, 2))
print(calculate_distance(80, 3)) #same problem using functions

size1 = 10
size2 = 20
size3 = 30
average_size = (size1 + size2 + size3) / 3
print(average_size) #example 2

def calculate_average_size(size1, size2, size3):
    return (size1 + size2 + size3) / 3
print(calculate_average_size(10, 20, 30)) #same problem using functions

area1 = 50
area2 = 75
area3 = 100
total_area = area1 + area2 + area3
print(total_area) #example 3

def calculate_total_area(area1, area2, area3):
    return area1 + area2 + area3
print(calculate_total_area(50, 75, 100)) #same problem using functions

weight1 = 150
height1 = 60
bmi1 = weight1 / (height1 ** 2)
print(bmi1) #example 4

def calculate_bmi(weight, height):
    return weight / (height ** 2)
print(calculate_bmi(150, 60)) #same problem using functions

temperature1 = 30
temperature2 = 25
temperature3 = 20
average_temperature = (temperature1 + temperature2 + temperature3) / 3
print(average_temperature) #example 5

def calculate_average_temperature(temp1, temp2, temp3):
    return (temp1 + temp2 + temp3) / 3
print(calculate_average_temperature(30, 25, 20)) #same problem using functions