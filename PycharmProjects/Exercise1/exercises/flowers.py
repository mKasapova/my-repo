ARANJIRANE = 2
sum = 0

hrisantems = int(input())
roses = int(input())
tulips = int(input())
season = input()
is_official = input()

if season in ("Spring", "Summer"):
    price_hrisantem = 2.00
    price_rouse = 4.10
    price_tulip = 2.50
elif season in ("Autumn", "Winter"):
    price_hrisantem = 3.75
    price_rouse = 4.50
    price_tulip = 4.15

sum = hrisantems * price_hrisantem + roses * price_rouse + tulips * price_tulip

if is_official == "Y":
    sum += sum * 0.15
    if tulips > 7 and season == "Spring":
        sum -= sum * 0.05
    elif roses >= 10 and season == "Winter":
        sum -= sum * 0.1
    elif hrisantems + roses + tulips > 20:
        sum -= sum * 0.2
else:
    if tulips > 7 and season == "Spring":
        sum -= sum * 0.05
    elif roses >= 10 and season == "Winter":
        sum -= sum * 0.1

if hrisantems + roses + tulips > 20:
    sum -= sum * 0.2

price = sum + ARANJIRANE

print(f"{price:.2f}")