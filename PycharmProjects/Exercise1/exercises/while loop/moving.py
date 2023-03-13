width = int(input())
length = int(input())
height = int(input())
volume = width * length * height
boxes = ""

while volume > 0:
    boxes = input()
    if boxes == "Done" and volume > 0:
        print(f"{volume} Cubic meters left.")
        break
    volume -= int(boxes)

if volume < 0:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")