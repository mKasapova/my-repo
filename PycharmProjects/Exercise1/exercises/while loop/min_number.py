number = input()
min = int(number)

while True:
    number = input()
    if number == "Stop":
        break
    if min > int(number):
        min = int(number)

print(min)