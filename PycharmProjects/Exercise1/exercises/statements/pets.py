import math

days = int(input())
food_kilos = int(input())
day_food_dog = float(input())
day_food_cat = float(input())
day_food_turtle_grams = float(input())

dog = days * day_food_dog
cat = days * day_food_cat
turtle = days * day_food_turtle_grams / 1000

all_food_needed = dog + cat + turtle

if food_kilos >= all_food_needed:
    food_left = food_kilos - all_food_needed
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    food_needed = all_food_needed - food_kilos
    print(f"{math.ceil(food_needed)} more kilos of food are needed.")

