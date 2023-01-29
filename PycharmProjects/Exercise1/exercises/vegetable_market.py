price_kilo_vegetable = float(input())
price_kilo_fruit = float(input())
all_kilos_vegetable = float(input())
all_kilos_fruits = float(input())

EURO_TO_BNG = 1.94

all_vegetables_price_euro = (all_kilos_vegetable * price_kilo_vegetable) / EURO_TO_BNG
all_fruits_price_euro = (all_kilos_fruits * price_kilo_fruit) / EURO_TO_BNG

all_price = all_fruits_price_euro + all_vegetables_price_euro

print(f"{all_price:.2f}")