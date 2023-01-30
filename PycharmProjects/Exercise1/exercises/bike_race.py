tax_juniors = 0
tax_seniors = 0

juniors = int(input())
seniors = int(input())
trace = input()

if trace == "trail":
    tax_juniors = 5.50
    tax_seniors = 7.0
elif trace == "cross-country" and 50 > juniors + seniors:
    tax_juniors = 8
    tax_seniors = 9.50
elif trace == "cross-country" and 50 <= juniors + seniors:
    tax_juniors = 8 - 8 * 0.25
    tax_seniors = 9.50 - 9.50 * 0.25
elif trace == "downhill":
    tax_juniors = 12.25
    tax_seniors = 13.75
elif trace == "road":
    tax_juniors = 20
    tax_seniors = 21.50

sum = tax_juniors * juniors + tax_seniors * seniors
razhodi = sum * 0.05
left = sum - razhodi

print(f"{left:.2f}")