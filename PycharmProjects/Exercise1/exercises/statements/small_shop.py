product = input()
city = input()
quantity = float(input())
price = 0

if city == "Sofia":
    coffee = 0.50
    water = 0.80
    beer = 1.20
    sweets = 1.45
    peanuts = 1.60
    if product == "coffee":
        price = coffee * quantity
    elif product == "water":
        price = water * quantity
    elif product == "beer":
        price = beer * quantity
    elif product == "sweets":
        price = sweets * quantity
    elif product == "peanuts":
        price = peanuts * quantity
elif city == "Plovdiv":
    coffee = 0.40
    water = 0.70
    beer = 1.15
    sweets = 1.30
    peanuts = 1.50
    if product == "coffee":
        price = coffee * quantity
    elif product == "water":
        price = water * quantity
    elif product == "beer":
        price = beer * quantity
    elif product == "sweets":
        price = sweets * quantity
    elif product == "peanuts":
        price = peanuts * quantity
elif city == "Varna":
    coffee = 0.45
    water = 0.70
    beer = 1.10
    sweets = 1.35
    peanuts = 1.55
    if product == "coffee":
        price = coffee * quantity
    elif product == "water":
        price = water * quantity
    elif product == "beer":
        price = beer * quantity
    elif product == "sweets":
        price = sweets * quantity
    elif product == "peanuts":
        price = peanuts * quantity

print(price)