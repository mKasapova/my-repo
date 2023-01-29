price_for_square_meter_nylon = 1.50
price_for_paint_liter = 14.50
price_paint_thinner_liter = 5.00
price_for_bags = 0.40

all_square_meters_nylon = int(input()) + 2
all_paint_liters = int(input())
all_paintThinner_liters = int(input())
working_hours = int(input())

all_extra_liters_paint = all_paint_liters + all_paint_liters * 0.1

final_sum_for_materials = all_square_meters_nylon * price_for_square_meter_nylon + all_extra_liters_paint * price_for_paint_liter + all_paintThinner_liters * price_paint_thinner_liter + price_for_bags

price_for_one_hour = final_sum_for_materials * 0.3

final_sum = final_sum_for_materials + working_hours * price_for_one_hour

print(final_sum)

