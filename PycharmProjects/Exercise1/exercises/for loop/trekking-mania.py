count_groups = int(input())
group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0
all_people = 0

for i in range(0, count_groups):
    count_people = int(input())
    all_people += count_people
    if count_people <= 5:
        group1 += count_people
    elif 6 <= count_people <= 12:
        group2 += count_people
    elif 13 <= count_people <= 25:
        group3 += count_people
    elif 26 <= count_people <= 40:
        group4 += count_people
    else:
        group5 += count_people


print(f"{((group1 / all_people) * 100):.2f}%")
print(f"{((group2 / all_people) * 100):.2f}%")
print(f"{((group3 / all_people) * 100):.2f}%")
print(f"{((group4 / all_people) * 100):.2f}%")
print(f"{((group5 / all_people) * 100):.2f}%")