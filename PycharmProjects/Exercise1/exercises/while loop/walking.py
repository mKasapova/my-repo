STEPS = 10_000
goal = 0

while True:
    walking = input()
    if walking == "Going home":
        walking = input()
        goal += int(walking)
        if goal < STEPS:
            print(f"{STEPS - goal} more steps to reach goal.")
            break
    if goal < STEPS:
        goal += int(walking)
    if goal >= STEPS:
        print(f"Goal reached! Good job!")
        print(f"{goal - STEPS} steps over the goal!")
        break
