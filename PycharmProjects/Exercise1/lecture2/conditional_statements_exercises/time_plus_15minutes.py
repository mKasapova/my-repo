hours = int(input())
minutes = int(input())

hours_to_minutes = hours * 60
total_minutes = hours_to_minutes + minutes + 15

total_hours = total_minutes // 60
end_minutes = total_minutes % 60

if total_hours == 24 and end_minutes < 10:
    print(f'0:0{end_minutes}')
elif total_hours == 24 and end_minutes >=10:
    print(f'0:{end_minutes}')
elif total_hours != 24 and end_minutes < 10:
    print(f'{total_hours}:0{end_minutes}')
else:
    print(f'{total_hours}:{end_minutes}')