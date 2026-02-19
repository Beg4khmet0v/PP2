numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled) #example of lambda with map

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared) #example 1

words = ["apple", "banana", "cherry"]
uppercased = list(map(lambda w: w.upper(), words))
print(uppercased) #example 2

words = ["dog", "elephant", "cat"]
lengths = list(map(lambda w: len(w), words))
print(lengths) #example 3

names = ["Alice", "Bob", "Charlie"]
greeted = list(map(lambda n: "Hello " + n, names))
print(greeted) #example 4

numbers = [10, 20, 30, 40]
as_strings = list(map(lambda x: str(x), numbers))
print(as_strings) #example 5