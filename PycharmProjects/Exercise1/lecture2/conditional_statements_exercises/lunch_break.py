import math

name = input()
duration_film = int(input())
duration_break = int(input())

lunch_time = duration_break / 8
time_relax = duration_break / 4

left_time = duration_break - (lunch_time + time_relax)

if left_time >= duration_film:
    left_time2 = left_time - duration_film
    print(f'You have enough time to watch {name} and left with {math.ceil(left_time2)} minutes free time.')
else:
    needed_time = duration_film - left_time
    print(f"You don't have enough time to watch {name}, you need {math.ceil(needed_time)} more minutes.")