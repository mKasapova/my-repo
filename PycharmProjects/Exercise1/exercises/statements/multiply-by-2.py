n = float(input())
res = 0

while n >= 0:
    res = n * 2
    print(f"Result: {res:.2f}")
    n = float(input())
else:
    print("Negative number!")
