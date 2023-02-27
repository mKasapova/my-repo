count_students = int(input())
students_grades = []
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
all_grades = 0

for i in range(0, count_students):
    students_grades.append(float(input()))

for i in range(0, len(students_grades)):
    all_grades += students_grades[i]
    if 2.00 <= students_grades[i] <= 2.99:
        count_2 += 1
    elif 3.00 <= students_grades[i] <= 3.99:
        count_3 += 1
    elif 4.00 <= students_grades[i] <= 4.99:
        count_4 += 1
    else:
        count_5 += 1

average = all_grades / count_students

print(f"Top students: {((count_5 / count_students) * 100):.2f}%")
print(f"Between 4.00 and 4.99: {((count_4 / count_students) * 100):.2f}%")
print(f"Between 3.00 and 3.99: {((count_3 / count_students) * 100):.2f}%")
print(f"Fail: {((count_2 / count_students) * 100):.2f}%")
print(f"Average: {average:.2f}")