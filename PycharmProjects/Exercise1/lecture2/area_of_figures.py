from math import pi

vid = input()
area = 0.0

if vid == "square":
    x = float(input())
    area = x * x
elif vid == "rectangle":
    x = float(input())
    y = float(input())
    area = x * y
elif vid == "circle":
    r = float(input())
    area = pi * r * r
elif vid == "triangle":
    a = float(input())
    h = float(input())
    area = (a * h) / 2

print(f"{area:.3f}")