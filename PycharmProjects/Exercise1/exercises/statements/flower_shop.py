import math

MAGNOLII = 3.25
ZYMBYLI = 4.0
ROSES = 3.50
CACTUS = 8.0

count_magnolii = int(input())
count_zymbyli = int(input())
count_roses = int(input())
count_cactus = int(input())
price_present = float(input())

price_order = count_magnolii * MAGNOLII + count_zymbyli * ZYMBYLI + count_roses * ROSES + count_cactus * CACTUS
final_price = price_order - price_order * 0.05

if final_price >= price_present:
    left = final_price - price_present
    print(f"She is left with {math.floor(left)} leva.")
else:
    need = price_present - final_price
    print(f"She will have to borrow {math.ceil(need)} leva.")