rouse = 5.0
daliya = 3.80
lale = 2.80
narcis = 3.0
gladiola = 2.50

type_flowers = input()
count = int(input())
budget = int(input())
price = 0.0

if type_flowers == "Roses":
    if count > 80:
        price = rouse * count - (rouse * count) * 0.1
    else:
        price = rouse * count
elif type_flowers == "Dahlias":
    if count > 90:
        price = daliya * count - (daliya * count) * 0.15
    else:
        price = daliya * count
elif type_flowers == "Tulips":
    if count > 80:
        price = lale * count - (lale * count) * 0.15
    else:
        price = lale * count
elif type_flowers == "Narcissus":
    if count < 120:
        price = narcis * count + (narcis * count) * 0.15
    else:
        price = narcis * count
elif type_flowers == "Gladiolus":
    if count < 80:
        price = gladiola * count + (gladiola * count) * 0.2
    else:
        price = gladiola * count

if price <= budget:
    left = budget - price
    print(f"Hey, you have a great garden with {count} {type_flowers} and {left:.2f} leva left.")
else:
    need = price - budget
    print(f"Not enough money, you need {need:.2f} leva more.")