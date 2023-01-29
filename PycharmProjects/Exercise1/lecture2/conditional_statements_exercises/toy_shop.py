PUZZLE = 2.60
TALKING_DOLL = 3.00
FLUFFY_BEAR = 4.10
MINYON = 8.20
TRUCK = 2.00

total_toys_price = 0.0

travel_price = float(input())
count_puzzles = int(input())
count_talking_dolls = int(input())
count_fluffy_bears = int(input())
count_minyons = int(input())
count_trucks = int(input())

total_count_toys = count_puzzles + count_talking_dolls + count_fluffy_bears + count_minyons + count_trucks
total_toys_price = count_puzzles * PUZZLE \
                    + count_talking_dolls * TALKING_DOLL \
                    + count_fluffy_bears * FLUFFY_BEAR \
                    + count_minyons * MINYON \
                    + count_trucks * TRUCK

if total_count_toys >= 50:
    total_toys_price = total_toys_price - total_toys_price * 0.25

money_after_naem = total_toys_price - total_toys_price * 0.1

if money_after_naem >= travel_price:
    left_money = money_after_naem - travel_price
    print(f'Yes! {left_money:.2f} lv left.')
else:
    needed_money = travel_price - money_after_naem
    print(f'Not enough money! {needed_money:.2f} lv needed.')
