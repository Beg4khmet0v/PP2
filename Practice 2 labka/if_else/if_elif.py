a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") #this is 1st example of if-elif structure from w3schools

number = -10
if number > 0:
  print("The number is positive")
elif number == 0:
  print("The number is zero") #1st example

c = 10
d = 20
if c > d:
    print("c is greater than d")
elif c == d:
    print("c is equal to d") #2nd example

e = 30
f = 15 
if e < f:
    print("e is less than f")
elif e != f:
    print("e is not equal to f") #3rd example

g = 50
h = 50
if g > h:
    print("g is greater than h")
elif g >= h:
    print("g is greater than or equal to h") #4th example

i = 75
j = 100
if i < j:
    print("i is less than j")
elif i <= j:
    print("i is less than or equal to j") #5th example

score = 75
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D") #this is 2nd example of if-elif structure from w3schools, but difference is in multiple elif blocks

age = 25
if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior") #another example with multiple elif blocks from w3schools

day = 3
if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday") #again, multiple elif blocks example from w3schools

symbol = '#'
if symbol == '!':
    print("Exclamation mark")
elif symbol == '@':
    print("At symbol")
elif symbol == '#':
    print("Hash symbol") #1st example

color = 'blue'
if color == 'red':
    print("The color is red")
elif color == 'green':
    print("The color is green")
elif color == 'blue':
    print("The color is blue") #2nd example

temperature = 15
if temperature > 30:    
    print("It's a hot day.")
elif temperature > 20:
    print("It's a warm day.")
elif temperature > 10:
    print("It's a cool day.") #3rd example

speed = 70
if speed > 100:
    print("You are driving too fast.")
elif speed > 60:
    print("You are driving at a moderate speed.") #4th example
elif speed <= 60:
    print("You are driving within the speed limit.")

budget = 500
if budget >= 1000:
    print("You can afford a luxury vacation.")
elif budget >= 500:
    print("You can afford a standard vacation.") #5th example
elif budget < 500:
    print("You can afford a budget vacation.")