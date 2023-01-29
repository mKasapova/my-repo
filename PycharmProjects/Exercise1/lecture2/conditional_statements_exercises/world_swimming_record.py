record_sec = float(input())
distance_meters = float(input())
secs_for_one_meter = float(input())

delay = (distance_meters // 15) * 12.5
time = secs_for_one_meter * distance_meters + delay

if time < record_sec:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
else:
    difference = time - record_sec
    print(f'No, he failed! He was {difference:.2f} seconds slower.')