failed_grades = int(input())

solved_tasks = 0
failed_times = 0
sum_grades = 0
last_task = ''
has_failed = True

while failed_times < failed_grades:
    task = input()
    if task == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    sum_grades += grade
    solved_tasks += 1
    last_task = task

if has_failed:
    print(f"You need a break, {failed_grades} poor grades.")
else:
    print(f"Average score: {sum_grades / solved_tasks:.2f}")
    print(f"Number of problems: {solved_tasks}")
    print(f"Last problem: {last_task}")

