number = input()
max = int(number)

while True:
    number = input()
    if number == "Stop":
        break
    if max < int(number):
        max = int(number)

print(max)