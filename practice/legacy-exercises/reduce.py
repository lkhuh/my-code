from functools import reduce

list = [1,3,5,6,87,97,54]
num = reduce(lambda x,y:x*y,list)
print(num)