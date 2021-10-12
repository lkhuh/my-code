def gen(n):
    for i in range(n):
         yield  i

g = gen(30000)
for i in g:
    print(i)

#   H = "sparsh"
# ier = iter(H)
# print(ier.__next__())
# print(ier.__next__())
# for C in H :
#     print(C)
