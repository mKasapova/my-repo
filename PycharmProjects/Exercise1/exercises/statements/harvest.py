import math

x_square_meters = int(input())
y_grapes_per_sqmeters = float(input())
z_liters_wine_needed = int(input())
workers = int(input())

total_grapes = y_grapes_per_sqmeters * x_square_meters
for_wine = total_grapes * 0.4
liters_wine = for_wine / 2.5

if liters_wine < z_liters_wine_needed:
    wine_need = z_liters_wine_needed - liters_wine
    print(f"It will be a tough winter! More {math.floor(wine_need)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(liters_wine)} liters.")
    left_wine = liters_wine - z_liters_wine_needed
    wine_per_worker = left_wine / workers
    print(f"{math.ceil(left_wine)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
