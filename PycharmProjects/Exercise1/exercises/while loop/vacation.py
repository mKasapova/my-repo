money_for_vacation = float(input())
available_money = float(input())
days = 0
count_spend = 0

while available_money < money_for_vacation and count_spend < 5:
    action = input()
    money_to_spend_save = float(input())
    days += 1
    if action == "spend":
        available_money -= money_to_spend_save
        count_spend += 1
        if available_money < 0:
            available_money= 0
    elif action == "save":
        available_money += money_to_spend_save
        count_spend = 0

if count_spend == 5:
    print(f"You can't save the money.")
    print(f"{days}")
if available_money >= money_for_vacation:
    print(f"You saved the money for {days} days.")