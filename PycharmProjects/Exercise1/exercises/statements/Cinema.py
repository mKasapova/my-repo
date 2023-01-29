premiere = 12.00
normal = 7.50
discount = 5.00

screening_type = input()
rows = int(input())
columns = int(input())
seats = rows * columns
price = 0

if screening_type == "Premiere":
    price = seats * premiere
elif screening_type == "Normal":
    price = seats * normal
elif screening_type == "Discount":
    price = seats * discount

print(f"{price:.2f} leva")