count = int(input())
sum_left = 0
sum_right = 0

for i in range(0, 2 * count):
    n = int(input())
    if i < count:
        sum_left = n + sum_left
    else:
        sum_right = n + sum_right

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    diff = abs(sum_left - sum_right)
    print(f"No, diff = {diff}")
