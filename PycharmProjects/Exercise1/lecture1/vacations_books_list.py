pages_in_book = int(input())
pages_for_one_hour = int(input())
days = int(input())

hours_to_read = int(pages_in_book / pages_for_one_hour)
hours_day = int(hours_to_read / days)

print(hours_day)
