month = input()
overnight_stay = int(input())
sum_one_night_studio = 0
sum_one_night_apartament = 0
sum_studio = 0
sum_apartament = 0

if month in ("May", "October"):
    if 7 < overnight_stay <= 14:
        sum_one_night_studio = 50 - 50 * 0.05
    elif overnight_stay > 14:
        sum_one_night_studio = 50 - 50 * 0.3
        sum_one_night_apartament = 65 - 65 * 0.1
    else:
        sum_one_night_studio = 50
        sum_one_night_apartament = 65
elif month in ("June", "September"):
    if overnight_stay > 14:
        sum_one_night_studio = 75.20 - 75.20 * 0.2
        sum_one_night_apartament = 68.70 - 68.70 * 0.1
    else:
        sum_one_night_studio = 75.20
        sum_one_night_apartament = 68.70
elif month in ("July", "August"):
    if overnight_stay > 14:
        sum_one_night_studio = 76
        sum_one_night_apartament = 77 - 77 * 0.1
    else:
        sum_one_night_studio = 76
        sum_one_night_apartament = 77

sum_studio = sum_one_night_studio * overnight_stay
sum_apartament = sum_one_night_apartament * overnight_stay

print(f"Apartment: {sum_apartament:.2f} lv.")
print(f"Studio: {sum_studio:.2f} lv.")


