exam_hour = int(input())
exam_minutes = int(input())
arrive_hour = int(input())
arrive_minutes = int(input())

arrive_in_minutes = arrive_hour * 60 + arrive_minutes
exam_in_minutes = exam_hour * 60 + exam_minutes

if arrive_in_minutes == exam_in_minutes or 0 < (exam_in_minutes - arrive_in_minutes) <= 30:
    print("On time")
elif (exam_in_minutes - arrive_in_minutes) > 30:
    print("Early")
elif exam_in_minutes - arrive_in_minutes < 0:
    print("Late")

if arrive_in_minutes <= exam_in_minutes - 1 or arrive_in_minutes >= exam_in_minutes + 1:
    if arrive_in_minutes < exam_in_minutes:
        if (exam_in_minutes - arrive_in_minutes) < 60:
            print(f"{exam_in_minutes - arrive_in_minutes} minutes before the start")
        elif (exam_in_minutes - arrive_in_minutes) >= 60:
            min_before = exam_in_minutes - arrive_in_minutes
            hour = int(min_before / 60)
            mm = min_before % 60
            if mm <= 9:
                print(f"{hour}:0{mm} hours before the start")
            else:
                print(f"{hour}:{mm} hours before the start")
    elif arrive_in_minutes > exam_in_minutes:
        if (arrive_in_minutes - exam_in_minutes) < 60:
            print(f"{arrive_in_minutes - exam_in_minutes} minutes after the start")
        elif (arrive_in_minutes - exam_in_minutes) >= 60:
            min_after = arrive_in_minutes - exam_in_minutes
            hour = int(min_after / 60)
            mm = min_after % 60
            if mm <= 9:
                print(f"{hour}:0{mm} hours after the start")
            else:
                print(f"{hour}:{mm} hours after the start")
