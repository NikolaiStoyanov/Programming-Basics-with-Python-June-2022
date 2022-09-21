book_looking_after = input()
checked_books = 0
books = input()
is_book_found = False
while books != "No More Books":

    if books == book_looking_after:
        is_book_found = True
        break

    checked_books += 1

    books = input()


if is_book_found:
    print(f"You checked {checked_books} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {checked_books} books.")
    # if books != book_looking_after:
    #
    #     print(f"You checked {checked_books} books and found it.")
    #
    #     checked_books += 1