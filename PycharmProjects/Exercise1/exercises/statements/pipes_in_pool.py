v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_full = p1 * h
p2_full = p2 * h
v1 = p1_full + p2_full
v1_percent = (v1 / v) * 100
p1_percent = (p1_full / v1) * 100
p2_percent = (p2_full / v1) * 100

if v1 <= v:
    print(f"The pool is {v1_percent:.2f}% full. Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.")
else:
    more_liters = v1 - v
    print(f"For {h} hours the pool overflows with {more_liters:.2f} liters.")