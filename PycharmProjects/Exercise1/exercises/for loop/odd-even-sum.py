count = int(input())
my_list = []
sum_odd = 0
sum_even = 0

for i in range(0, count):
    n = int(input())
    my_list.append(n)

for i in range(0, len(my_list)):
    if i % 2 == 0:
        sum_odd = my_list[i] + sum_odd
    else:
        sum_even = my_list[i] + sum_even

if sum_odd == sum_even:
    print("Yes")
    print(f"Sum = {sum_even}")
else:
    diff = abs(sum_odd - sum_even)
    print("No")
    print(f"Diff = {diff}")
