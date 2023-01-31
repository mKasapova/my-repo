season = input()
group = input()
students = int(input())
nights = int(input())

price_one_night_bg = 0
price_one_night_mix = 0

sport_girls = ""
sport_boys = ""
sport_mix = ""
sum = 0

if season == "Winter":
    price_one_night_bg = 9.60
    price_one_night_mix = 10
    sport_girls = "Gymnastics"
    sport_boys = "Judo"
    sport_mix = "Ski"
    if group == "boys" or group == "girls":
        sum = students * nights * price_one_night_bg
    else:
        sum = students * nights * price_one_night_mix
elif season == "Spring":
    price_one_night_bg = 7.20
    price_one_night_mix = 9.50
    sport_girls = "Athletics"
    sport_boys = "Tennis"
    sport_mix = "Cycling"
    if group == "boys" or group == "girls":
        sum = students * nights * price_one_night_bg
    else:
        sum = students * nights * price_one_night_mix
else:
    price_one_night_bg = 15
    price_one_night_mix = 20
    sport_girls = "Volleyball"
    sport_boys = "Football"
    sport_mix = "Swimming"
    if group == "boys" or group == "girls":
        sum = students * nights * price_one_night_bg
    else:
        sum = students * nights * price_one_night_mix

if 10 <= students < 20:
    sum -= sum * 0.05
elif 20 <= students < 50:
    sum -= sum * 0.15
elif 50 <= students:
    sum -= sum * 0.5

if group == "girls" and season == "Winter":
    print(f"{sport_girls} {sum:.2f} lv.")
elif group == "girls" and season == "Spring":
    print(f"{sport_girls} {sum:.2f} lv.")
elif group == "girls" and season == "Summer":
    print(f"{sport_girls} {sum:.2f} lv.")
elif group == "boys" and season == "Winter":
    print(f"{sport_boys} {sum:.2f} lv.")
elif group == "boys" and season == "Spring":
    print(f"{sport_boys} {sum:.2f} lv.")
elif group == "boys" and season == "Summer":
    print(f"{sport_boys} {sum:.2f} lv.")
elif group == "mixed" and season == "Winter":
    print(f"{sport_mix} {sum:.2f} lv.")
elif group == "mixed" and season == "Spring":
    print(f"{sport_mix} {sum:.2f} lv.")
elif group == "mixed" and season == "Summer":
    print(f"{sport_mix} {sum:.2f} lv.")