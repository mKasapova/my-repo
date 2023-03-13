width = int(input())
length = int(input())
pieces = ""
all_cake_pieces = width * length

while all_cake_pieces > 0:
    pieces = input()
    if pieces == "STOP" and all_cake_pieces > 0:
        print(f"{all_cake_pieces} pieces are left.")
        break
    all_cake_pieces -= int(pieces)

if all_cake_pieces < 0:
    print(f"No more cake left! You need {abs(all_cake_pieces)} pieces more.")


