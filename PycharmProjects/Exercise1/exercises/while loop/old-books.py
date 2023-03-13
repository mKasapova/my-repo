book_to_find = input()
count_books = 0

while True:
    book = input()
    if book == book_to_find:
        print(f"You checked {count_books} books and found it.")
        break
    elif book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {count_books} books.")
        break
    else:
        count_books += 1
        continue
