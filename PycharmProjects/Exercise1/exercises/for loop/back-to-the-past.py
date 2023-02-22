money = float(input())
year_must_live = int(input())
year = 17
money_1 = money

for i in range(1800, year_must_live+1):
    year += 1
    if i % 2 == 0:
        money_1 = money_1 - 12_000
    else:
        money_1 = money_1 - (12_000 + 50 * year)

if money_1 >= 0:
    print(f"Yes! He will live a carefree life and will have {(money_1):.2f} dollars left.")
else:
    money_1 = abs(money_1)
    print(f"He will need {money_1:.2f} dollars to survive.")