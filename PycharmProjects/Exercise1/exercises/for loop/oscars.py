name_actor = input()
points = float(input())
count_judges = int(input())

for i in range(0, count_judges):
    name_judge = input()
    points_from_judge = float(input())
    points = points + (len(name_judge) * points_from_judge) / 2

    if points >= 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {points:.1f}!")
        break
    else:
        continue

if points < 1250.5:
    print(f"Sorry, {name_actor} you need {(1250.5 - points):.1f} more!")
