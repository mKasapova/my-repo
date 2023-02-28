stadium_capacity = int(input())
all_fans = int(input())
sectors = []
fansA = 0
fansB = 0
fansV = 0
fansG = 0

for i in range(0, all_fans):
    sectors.append(input())

for i in range(0, len(sectors)):
    if sectors[i] == "A":
        fansA += 1
    elif sectors[i] == "B":
        fansB += 1
    elif sectors[i] == "V":
        fansV += 1
    elif sectors[i] == "G":
        fansG += 1

percentA = (fansA / all_fans) * 100
percentB = (fansB / all_fans) * 100
percentV = (fansV / all_fans) * 100
percentG = (fansG / all_fans) * 100
percent_fans = (all_fans / stadium_capacity) * 100

print(f"{percentA:.2f}%")
print(f"{percentB:.2f}%")
print(f"{percentV:.2f}%")
print(f"{percentG:.2f}%")
print(f"{percent_fans:.2f}%")