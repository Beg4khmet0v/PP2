from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map → square numbers
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# filter → even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# reduce → sum
total = reduce(lambda a, b: a + b, numbers)
print("Sum:", total)