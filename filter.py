num = [1,2,3,4,5,6,7,8,9]

def sparsh(number):
    return number>5
greater = list(filter(sparsh, num))
print(greater)