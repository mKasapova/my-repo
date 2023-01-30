VIP = 499.99
NORMAL = 249.99

budget = float(input())
category = input()
count_people = int(input())

sum_transport = 0

if 1 <= count_people <= 4:
    sum_transport = budget * 0.75
elif 5 <= count_people <= 9:
    sum_transport = budget * 0.6
elif 10 <= count_people <= 24:
    sum_transport = budget * 0.5
elif 25 <= count_people <= 49:
    sum_transport = budget * 0.4
else:
    sum_transport = budget * 0.25

left_for_tickets = budget - sum_transport

if category == "VIP":
    sum = VIP * count_people
elif category == "Normal":
    sum = NORMAL * count_people

diff = abs(left_for_tickets - sum)

if left_for_tickets >= sum:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
