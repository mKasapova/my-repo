points_begin = int(input())
bonus = 0

if points_begin <= 100:
    bonus = 5
elif 100 < points_begin <= 1000:
    bonus = points_begin * 0.2
elif points_begin > 1000:
    bonus = points_begin * 0.1

if points_begin % 2 == 0:
    bonus = bonus + 1
elif points_begin % 10 == 5:
    bonus = bonus + 2

total_points = points_begin + bonus

print(f'{bonus}')
print(f'{total_points}')