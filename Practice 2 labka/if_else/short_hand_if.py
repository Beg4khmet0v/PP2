a = 5
b = 2
if a > b: print("a is greater than b") #this is 1st example from w3schools

number = 8
if number % 2 == 0: print("The number is even") #1st example

c = 12
d = 15
if c < d: print("c is less than d") #2nd example

e = 25
f = 30
if e != f: print("e is not equal to f") #3rd example

g = 40
h = 35
if g >= h: print("g is greater than or equal to h") #4th example

i = 20
j = 20
if i <= j: print("i is less than or equal to j") #5th example

a = 2
b = 330
print("A") if a > b else print("B") #this is 2nd example from w3schools, without using if-else block

number = 10
print("Even") if number % 2 == 0 else print("Odd") #1st example

c = 5
d = 10
print("c is less than d") if c < d else print("c is not less than d") #2nd example

e = 15
f = 20
print("e is not equal to f") if e != f else print("e is equal to f") #3rd example

g = 25
h = 20
print("g is greater than or equal to h") if g >= h else print("g is less than h") #4th example

i = 30
j = 30
print("i is less than or equal to j") if i <= j else print("i is greater than j") #5th example


a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger) #this is 3rd example from w3schools, without using if-else block, but assigning value to a variable

number = 15
result = "Positive" if number > 0 else "Non-positive"
print("The number is", result) #1st example

c = 8
d = 12
larger = c if c > d else d
print("Larger is", larger) #2nd example

e = 18
f = 25
max_value = e if e > f else f
print("Max value is", max_value) #3rd example

g = 30
h = 22
higher = g if g > h else h
print("Higher is", higher) #4th example

i = 14
j = 14
equal_or_value = i if i == j else j
print("Equal or value is", equal_or_value) #5th example

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") #this is 4th example from w3schools, using multiple conditions in shorthand if-else

number = -5
print("Positive") if number > 0 else print("Zero") if number == 0 else print("Negative") #1st example

c = 10
d = 20
print("c is greater") if c > d else print("c and d are equal") if c == d else print("d is greater") #2nd example

e = 15
f = 15
print("e is less") if e < f else print("e and f are equal") if e == f else print("f is less") #3rd example

g = 25
h = 30
print("g is greater") if g > h else print("g and h are equal") if g == h else print("h is greater") #4th example

i = 40
j = 35
print("i is less") if i < j else print("i and j are equal") if i == j else print("i is greater") #5th example

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value) # Example of shorthand if-else which is useful in practical scenarios like finding maximum value

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name) # Example of shorthand if-else to provide default values, as before, for practical scenarios

temperature = 22
status = "Hot" if temperature > 25 else "Warm" if temperature >= 15 else "Cold"
print("The weather is", status) #1st example

score = 75
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print("Your grade is", grade) #2nd example

age = 30
life_stage = "Child" if age < 13 else "Teenager" if age < 20 else "Adult" if age < 65 else "Senior"
print("You are an", life_stage) #3rd example

income = 50000
tax_bracket = "Low" if income < 30000 else "Middle" if income < 100000 else "High"
print("Your tax bracket is", tax_bracket) #4th example

hours_worked = 45
overtime = "Yes" if hours_worked > 40 else "No"
print("Overtime worked:", overtime) #5th example

