budget = float(input())
season = input()
place = ""
where = ""
price = 0

if budget <= 100:
    place = "Bulgaria"
    if season == "summer":
        where = "Camp"
        price = budget * 0.3
    elif season == "winter":
        where = "Hotel"
        price = budget * 0.7
elif 100 < budget <= 1000:
    place = "Balkans"
    if season == "summer":
        where = "Camp"
        price = budget * 0.4
    elif season == "winter":
        where = "Hotel"
        price = budget * 0.8
elif budget > 1000:
    place = "Europe"
    where = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {place}")
print(f"{where} - {price:.2f}")

