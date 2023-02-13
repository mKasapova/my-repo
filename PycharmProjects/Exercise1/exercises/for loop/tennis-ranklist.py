import math
count_turnirs = int(input())
start_points = int(input())
count_wins = 0
final_points = 0
average_points = 0
points = 0

for i in range(0, count_turnirs):
    etap = input()
    if etap == "W":
        count_wins += 1
        points += 2000
    elif etap == "F":
        points += 1200
    elif etap == "SF":
        points += 720

final_points = start_points + points
average_points = (final_points - start_points) / count_turnirs
percent_wins = (count_wins / count_turnirs) * 100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percent_wins:.2f}%")