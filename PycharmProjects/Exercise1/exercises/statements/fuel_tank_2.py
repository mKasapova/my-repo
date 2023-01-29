price_gasoline = 2.22
price_diesel = 2.33
price_gas = 0.93
final_price = 0.0
price = 0.0

fuel = input()
fuel_in_liters = float(input())
discount_card = input()

if discount_card == "Yes":
    price_gasoline = price_gasoline - 0.18
    price_diesel = price_diesel - 0.12
    price_gas = price_gas - 0.08
    if fuel == "Gasoline":
        price = price_gasoline * fuel_in_liters
        if 20 < fuel_in_liters <= 25:
            final_price = price - price * 0.08
        elif fuel_in_liters > 25:
            final_price = price - price * 0.1
        else:
            final_price = price
    elif fuel == "Diesel":
        price = price_diesel * fuel_in_liters
        if 20 < fuel_in_liters <= 25:
            final_price = price - price * 0.08
        elif fuel_in_liters > 25:
            final_price = price - price * 0.1
        else:
            final_price = price
    elif fuel == "Gas":
        price = price_gas * fuel_in_liters
        if 20 < fuel_in_liters <= 25:
            final_price = price - price * 0.08
        elif fuel_in_liters > 25:
            final_price = price - price * 0.1
        else:
            final_price = price
else:
    if fuel == "Gasoline":
        price = price_gasoline * fuel_in_liters
        if 20 < fuel_in_liters <= 25:
            final_price = price - price * 0.08
        elif fuel_in_liters > 25:
            final_price = price - price * 0.1
        else:
            final_price = price
    elif fuel == "Diesel":
        price = price_diesel * fuel_in_liters
        if 20 < fuel_in_liters <= 25:
            final_price = price - price * 0.08
        elif fuel_in_liters > 25:
            final_price = price - price * 0.1
        else:
            final_price = price
    elif fuel == "Gas":
        price = price_gas * fuel_in_liters
        if 20 < fuel_in_liters <= 25:
            final_price = price - price * 0.08
        elif fuel_in_liters > 25:
            final_price = price - price * 0.1
        else:
            final_price = price

print(f"{final_price:.2f} lv.")