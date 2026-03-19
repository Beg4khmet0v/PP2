names = ["Ali", "Dana", "Arman"]
scores = [85, 90, 78]

# enumerate
for index, name in enumerate(names):
    print(index, name)

# zip
paired = list(zip(names, scores))
print("Paired:", paired)

# sorted
sorted_scores = sorted(scores)
print("Sorted scores:", sorted_scores)

# type conversion
num_str = "123"
num_int = int(num_str)
print(type(num_int))