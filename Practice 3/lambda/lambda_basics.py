x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) #three examples of same thing: how lambda works

y = lambda b: b * 2
print(y(7)) #my example

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11)) #example that function definition to make a function that always doubles the number you send in

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11)) #same code, but now, it triples.

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11)) #same, using both

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(4)

print(mytripler(11)) #my example