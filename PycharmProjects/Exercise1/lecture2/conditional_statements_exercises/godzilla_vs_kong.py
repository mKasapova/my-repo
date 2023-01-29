budget = float(input())
count_statisti = int(input())
price_clothes_per_one = float(input())

decor = budget * 0.1
total_price_clothes = count_statisti * price_clothes_per_one

if count_statisti > 150:
    total_price_clothes = total_price_clothes - total_price_clothes * 0.1

if decor + total_price_clothes > budget:
    needed_money = (decor + total_price_clothes) - budget
    print(f'Not enough money!')
    print(f'Wingard needs {needed_money:.2f} leva more.')
elif decor + total_price_clothes <= budget:
    left_money = budget - (decor + total_price_clothes)
    print(f'Action!')
    print(f'Wingard starts filming with {left_money:.2f} leva left.')