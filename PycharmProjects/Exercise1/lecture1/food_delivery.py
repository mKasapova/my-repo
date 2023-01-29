chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
delivery = 2.50

count_chicken_menus = int(input())
count_fish_menus = int(input())
count_vegan_menus = int(input())

price_all_menus = chicken_menu * count_chicken_menus + fish_menu * count_fish_menus + vegan_menu * count_vegan_menus
price_desert = price_all_menus * 0.2
final_price = price_all_menus + price_desert + delivery

print(round(final_price, 2))
