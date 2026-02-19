numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers) #example of lambda with filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) #example 1

words = ["apple", "banana", "cherry", "date"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words) #example 2

numbers = [10, 15, 20, 25, 30]
greater_than_20 = list(filter(lambda x: x > 20, numbers))
print(greater_than_20) #example 3

words = ["dog", "elephant", "cat", "tiger"]
starts_with_c = list(filter(lambda w: w.startswith("c"), words))
print(starts_with_c) #example 4

numbers = [-3, -1, 0, 2, 5, -7]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers) #example 5

