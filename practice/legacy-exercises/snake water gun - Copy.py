import random
sparsh = 1
print("number of chances is limited to only 9 times")
while sparsh <= 9 :
    sparsh = sparsh+1

game = int(input("write 1 for rock and 2 for paper , 3 for scissor\n"))
print(game)
if game == 1:
    print("rock")
elif game == 2:
    print("paper")
elif game == 3:
    print("scissor")
else:
    print("an error occured")

# r = ("rock")
# p = ("paper")
# s = ("scissor")

mygame = ("rock","paper","scissor")
op = random.choice(mygame)
print(op)
















