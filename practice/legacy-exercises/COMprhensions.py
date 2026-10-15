# list comprhensions
# ls = [i for i in range(100) if i%3==0]
# print(ls)

# dictionary comprhensions
# dict1 = { i:f" item {i}" for i in range(1 ,1000) }
# dict1 = {value:key for key,value in dict1.items()}
# print(dict1)

# generatorrs comprhensions
evens = (i for i in range (102) if i % 2 == 0)
# print(evens.__next__())
for i in evens:
    print(i)