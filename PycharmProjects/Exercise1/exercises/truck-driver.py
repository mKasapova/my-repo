season = input()
km_in_month = float(input())
salary = 0
sum = 0
price = 0

if km_in_month <= 5000:
    if season in ("Spring", "Autumn"):
        price = 0.75
    elif season == "Summer":
        price = 0.9
    else:
        price = 1.05
if 5000 < km_in_month <= 10_000:
    if season in ("Spring", "Autumn"):
        price = 0.95
    elif season == "Summer":
        price = 1.1
    else:
        price = 1.25
elif 10_000 < km_in_month <= 20_000:
    price = 1.45

sum = km_in_month * price * 4
salary = sum - sum * 0.1

print(f"{salary:.2f}")