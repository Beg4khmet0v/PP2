def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") #example from w3schools.com

def cars(*cars):
  print("My favorite cars are, "  *cars[2])

cars("Dodge Hellcat/Challenger/Charger", "Camaro Chevrolet", "Ford Mustang") #example

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus") #example of *args fro, w3schools

def my_name_is(*args):
  print("Type:", type(args))
  print("First Name: ", args[0])
  print("Second Name: ", args[1])
  print("Last Name: ", args)

my_name_is("Nurali", "Begakhmetov", "Dauletuli") #my example

def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus") #example of args with regular arguments

def my_function(hello, *names):
  for name in names:
    print(hello, name)

my_function("Wassup", "Nurik", "Beka", "Aldik") #my example

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5)) #practical example of *args that calculates the sum of any number of values 

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1)) #practical exmaple of *args of Finding the maximum value

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") #example of **kwargs

def my_function(**cars):
  print("Favorite car is " + cars["mark"])

my_function(fcar = "For Mustang", mark = "2012") #my example

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen") #again, just another one example of **kwargs

def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding") #**kwargs with regular arguments

def my_function(consumer, **features):
  print("Consumer name: ", consumer)
  print("Some features: ")
  for key, value in features.items():
    print(" ", key + ":", value)

my_function("Medet", height = 182, weight = 75) #my example

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo") #example of combining *args and **kwargs

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result) #example of unpacking arguments(list with *)

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes"), example of Using ** to unpack a dictionary into keyword arguments

def show_info(city, country):
    print("Location:", city, country)

place = {"city": "Paris", "country": "France"}
show_info(**place) #my example