books = [ ]

print("입력을 종료하려면 [Enter] 키를 누르시오.")

while True:
    book = input("도서명 입력: ")
    if not book:
        break
    books.append(book.strip())

books.sort()

for book in books:
    print(book)
