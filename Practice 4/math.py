import math

# 1
degree = 15
radian = math.radians(degree)
print(radian)

# 2
height = 5
base1 = 5
base2 = 6
area_trapezoid = ((base1 + base2) / 2) * height
print(area_trapezoid)

# 3
n_sides = 4
side_length = 25
area_polygon = (n_sides * side_length**2) / (4 * math.tan(math.pi / n_sides))
print(area_polygon)

# 4
base = 5
height_para = 6
area_para = base * height_para
print(area_para)