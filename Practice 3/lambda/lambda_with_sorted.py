students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students) #example of Sort a list of tuples by the second element

products = [("Laptop", 1200), ("Phone", 800), ("Tablet", 600)]
sorted_products = sorted(products, key=lambda x: x[1])
print(sorted_products) #example 1

cities = [("Paris", 2), ("London", 5), ("Berlin", 3)]
sorted_cities = sorted(cities, key=lambda x: x[1])
print(sorted_cities) #example 2

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_scores = sorted(scores, key=lambda x: x[1])
print(sorted_scores) #example 3

books = [("Book A", 300), ("Book B", 150), ("Book C", 450)]
sorted_books = sorted(books, key=lambda x: x[1])
print(sorted_books) #example 4

movies = [("Movie X", 7.5), ("Movie Y", 8.2), ("Movie Z", 6.9)]
sorted_movies = sorted(movies, key=lambda x: x[1])
print(sorted_movies) #example 5

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words) #example of Sort strings by length

animals = ["dog", "elephant", "cat", "tiger"]
sorted_animals = sorted(animals, key=lambda x: len(x))
print(sorted_animals) #example 1

fruits = ["kiwi", "watermelon", "pear", "grape"]
sorted_fruits = sorted(fruits, key=lambda x: len(x))
print(sorted_fruits) #example 2

colors = ["red", "blue", "yellow", "green"]
sorted_colors = sorted(colors, key=lambda x: len(x))
print(sorted_colors) #example 3

countries = ["USA", "Germany", "India", "Australia"]
sorted_countries = sorted(countries, key=lambda x: len(x))
print(sorted_countries) #example 4

cars = ["BMW", "Mercedes", "Volkswagen", "Audi"]
sorted_cars = sorted(cars, key=lambda x: len(x))
print(sorted_cars) #example 5