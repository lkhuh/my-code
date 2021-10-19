f = open("sparsh10.txt")

try:
    f = open("does.txt")
except Exception as e:
    print(e)
else:
    print("this will run only if try statement is not running")
finally:
    print("run this anyway ")
    print("important stuff")
