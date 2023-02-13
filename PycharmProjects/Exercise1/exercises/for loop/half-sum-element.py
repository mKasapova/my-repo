import sys

n = int(input())
sum_numbers = 0
max_number = -sys.maxsize

for i in range(0, n):
    num = int(input())
    if num > max_number:
        max_number = num

    sum_numbers += num

if max_number == (sum_numbers - max_number):
    print("Yes")
    print(f"Sum = {sum_numbers - max_number}")
else:
    print("No")
    sum_others = sum_numbers - max_number
    diff = abs(max_number - sum_others)
    print(f"Diff = {diff}")

