name = input()
grade = 0
sum = 0
count = 0
average = 0

while True:
    mark = float(input())
    if mark < 4:
        count += 1
        if count == 2:
            grade += 1
            print(f"{name} has been excluded at {grade} grade")
            break
    else:
        grade += 1
        sum += mark
    if grade == 12:
        average = sum / grade
        print(f"{name} graduated. Average grade: {average:.2f}")
        break


