ROOM_FOR_ONE_PERSON = 18.00
APARTAMENT = 25.00
PRESIDENT_APARTAMENT = 35.00

days = int(input())
room = input()
mark = input()

count_overnight_stay = days - 1
price = 0

if days < 10:
    if room == "apartment":
        price = APARTAMENT * count_overnight_stay - (APARTAMENT * count_overnight_stay) * 0.3
    elif room == "president apartment":
        price = PRESIDENT_APARTAMENT * count_overnight_stay - (PRESIDENT_APARTAMENT * count_overnight_stay) * 0.1
    else:
        price = ROOM_FOR_ONE_PERSON * count_overnight_stay
elif 10 <= days <= 15:
    if room == "apartment":
        price = APARTAMENT * count_overnight_stay - (APARTAMENT * count_overnight_stay) * 0.35
    elif room == "president apartment":
        price = PRESIDENT_APARTAMENT * count_overnight_stay - (PRESIDENT_APARTAMENT * count_overnight_stay) * 0.15
    else:
        price = ROOM_FOR_ONE_PERSON * count_overnight_stay
else:
    if room == "apartment":
        price = APARTAMENT * count_overnight_stay - (APARTAMENT * count_overnight_stay) * 0.5
    elif room == "president apartment":
        price = PRESIDENT_APARTAMENT * count_overnight_stay - (PRESIDENT_APARTAMENT * count_overnight_stay) * 0.2
    else:
        price = ROOM_FOR_ONE_PERSON * count_overnight_stay


if mark == "positive":
    price = price + price * 0.25
else:
    price = price - price * 0.1

print(f"{price:.2f}")

