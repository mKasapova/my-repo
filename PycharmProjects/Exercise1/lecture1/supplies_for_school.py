pens_package_price = 5.80
markers_package_price = 7.20
clean_stuff_one_liter_price = 1.20

count_pens_packages = int(input())
count_markers_packages = int(input())
liters_clean_stuff = int(input())
discount_percent = int(input()) / 100

all_sum = count_pens_packages * pens_package_price + count_markers_packages * markers_package_price + liters_clean_stuff * clean_stuff_one_liter_price
discount = all_sum * discount_percent

price_with_discount = all_sum - discount

print(price_with_discount)
