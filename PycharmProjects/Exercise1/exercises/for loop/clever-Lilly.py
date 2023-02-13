age = int(input())
price = float(input())
price_toy = int(input())
save_money = 0
bday_money = 0
sum_toys = 0
count_bdays = 0
count_toys = 0

for i in range(1, age+1):
    if i % 2 == 0:
        bday_money = bday_money + 10 
        save_money += bday_money
        count_bdays += 1
    else:
        count_toys += 1

sum_toys = count_toys * price_toy
save_money = (save_money + sum_toys) - count_bdays * 1
if save_money > price:
    print(f"Yes! {(save_money - price):.2f}")
else:
    print(f"No! {abs(save_money - price):.2f}")
