tabs = int(input())
salary = int(input())


for i in range(0, tabs):
    site = input()
    if site == "Facebook":
        salary = salary - 150
    elif site == "Instagram":
        salary = salary - 100
    elif site == "Reddit":
        salary = salary - 50
    else:
        continue

    if salary <= 0:
        print("You have lost your salary.")
        break
    
if salary > 0:
    print(salary)