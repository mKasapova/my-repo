count = int(input())
my_list = []


for i in range(0, count):
    n = int(input())
    my_list.append(n)

max = my_list[0]
for i in range(1, len(my_list)):
    if max < my_list[i]:
        max = my_list[i]
    else:
        continue

min = my_list[0]
for i in range(1, len(my_list)):
    if min > my_list[i]:
        min = my_list[i]
    else:
        continue

print(f"Max number: {max}")
print(f"Min number: {min}")
