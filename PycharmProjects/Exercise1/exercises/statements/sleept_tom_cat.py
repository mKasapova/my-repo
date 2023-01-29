TIME_WORK = 63
TIME_RELAX = 127
TIME_MAX = 30000
relax_days = int(input())
work_days = 365 - relax_days
total_time = relax_days * TIME_RELAX + work_days * TIME_WORK

if total_time > TIME_MAX:
    difference = total_time - TIME_MAX
    hours = difference // 60
    min = difference % 60
    print("Tom will run away")
    print(f"{hours} hours and {min} minutes more for play")
else:
    difference = TIME_MAX - total_time
    hours = difference // 60
    min = difference % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {min} minutes less for play")
