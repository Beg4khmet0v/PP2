# 1
def gen_squares(n):
    for i in range(n+1):
        yield i*i

for x in gen_squares(5):
    print(x)

# 2
def gen_even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = 10
print(",".join(str(x) for x in gen_even(n)))

# 3
def gen_div34(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for x in gen_div34(50):
    print(x)

# 4
def squares(a, b):
    for i in range(a, b+1):
        yield i*i

for val in squares(3, 7):
    print(val)

# 5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

for x in countdown(5):
    print(x)