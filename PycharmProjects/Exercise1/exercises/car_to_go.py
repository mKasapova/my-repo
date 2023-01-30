budget = float(input())
season = input()
price = 0
clas = ""
car = ""

if budget <= 100:
    clas = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.35
    else:
        car = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    clas = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.45
    else:
        car = "Jeep"
        price = budget * 0.80
else:
    clas = "Luxury class"
    car = "Jeep"
    price = budget * 0.9

print(f"{clas}")
print(f"{car} - {price:.2f}")
