budget = float(input())
season = input()
type = ""
price = 0
place = ""

if budget <= 1000:
    type = "Camp"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.65
    else:
        place = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    type = "Hut"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.8
    else:
        place = "Morocco"
        price = budget * 0.6
else:
    type = "Hotel"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.9
    else:
        place = "Morocco"
        price = budget * 0.9

print(f"{place} - {type} - {price:.2f}")