budget = int(input())
season = input()
fishers = int(input())
sum = 0

if season == "Spring":
    sum = 3000
    if fishers <= 6:
        sum -= sum * 0.1
    elif 7 <= fishers <= 11:
        sum -= sum * 0.15
    elif fishers >= 12:
        sum -= sum * 0.25
elif season == "Summer" or season == "Autumn":
    sum = 4200
    if fishers <= 6:
        sum -= sum * 0.1
    elif 7 <= fishers <= 11:
        sum -= sum * 0.15
    elif fishers >= 12:
        sum -= sum * 0.25
elif season == "Winter":
    sum = 2600
    if fishers <= 6:
        sum -= sum * 0.1
    elif 7 <= fishers <= 11:
        sum -= sum * 0.15
    elif fishers >= 12:
        sum -= sum * 0.25

if fishers % 2 == 0:
    if season != "Autumn":
        sum -= sum * 0.05

diff = abs(sum - budget)

if sum <= budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")