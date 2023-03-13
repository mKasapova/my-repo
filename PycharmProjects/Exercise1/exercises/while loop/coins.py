money = float(input())
money_to_cents = int(money * 100)
coins = 0

while money_to_cents > 0:
    if money_to_cents >= 200:
        money_to_cents -= 200
        coins += 1
    elif money_to_cents >= 100:
        money_to_cents -= 100
        coins += 1
    elif money_to_cents >= 50:
        money_to_cents -= 50
        coins += 1
    elif money_to_cents >= 20:
        money_to_cents -= 20
        coins += 1
    elif money_to_cents >= 10:
        money_to_cents -= 10
        coins += 1
    elif money_to_cents >= 5:
        money_to_cents -= 5
        coins += 1
    elif money_to_cents >= 2:
        money_to_cents -= 2
        coins += 1
    elif money_to_cents >= 1:
        money_to_cents -= 1
        coins += 1

print(coins)