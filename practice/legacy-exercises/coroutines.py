import time
def searcher():
    time.sleep(4)
    book = "this is a book on code with harry and sparsh and joker"

    while True:
        text = (yield )

        if text in book:
            print("your text is in the book")
        else:
            print("your text is not in the book")
search = searcher()
print("search started")
next(search)
search.send("harry")
input("press any key")
search.send("sparsh")
input("press any key")
search.send("not")