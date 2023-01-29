n = int(input())
text = input()

if n < 20 and text == "day":
    begin_price = 0.7
    day_tax = 0.79
    total_price = begin_price + n * day_tax
    print(f"{total_price:.2f}")
elif n < 20 and text == "night":
    begin_price = 0.7
    night_tax = 0.90
    total_price = begin_price + n * night_tax
    print(f"{total_price:.2f}")
elif 20 <= n < 100:
    total_price = n * 0.09
    print(f"{total_price:.2f}")
else:
    total_price = n * 0.06
    print(f"{total_price:.2f}")
