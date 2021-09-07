import random
i = 0
computer_points = 0
human_points = 0
number_of_chance = 0
chance = 10
print("number of chances is limited to only 9 times ")
while number_of_chance < chance :
    number_of_chance = number_of_chance + 1


game = int(input("write 1 for rock and 2 for paper , 3 for scissor \n"))
print(game)
if game == 1:
    print("rock")
elif game == 2:
    print("paper")
elif game == 3:
    print("scissor")
else:
    print("an error occured")

r = ("rock")
p = ("paper")
s = ("scissor")

mygame = ("r","p","s")
op = random.choice(mygame)



if game == op:
    print("tie both 0 point to each \n")

elif game == 1 and op == "p":
    print(f"your guess is {game} and computer guess is {op} \n ")
    print(f"your point is {human_points} and computer point is {computer_points} \n")
    print("computer wins")
    computer_points = computer_points + 1
elif game == 1 and op == "s":
    print(f"your guess is {game} and computer guess is {op} \n ")
    print(f"your point is {human_points} and computer point is {computer_points} \n")
    print("human  wins")
    human_points = human_points + 1
elif game == 2 and op == "r":
    print(f"your guess is {game} and computer guess is {op} \n")
    print(f"your point is {human_points} and computer point is {computer_points} \n")
    print("human wins")
    human_points = human_points +  1

elif game == 2 and op == "s":
    print(f"your guess is {game} and computer guess is {op} \n ")
    print(f"your point is {human_points} and computer point is {computer_points} \n")
    print("computer wins")
    computer_points = computer_points + 1

elif game == 3 and op == "r":
    print(f"your guess is {game} and computer guess is {op} \n ")
    print(f"your point is {human_points} and computer point is {computer_points} \n")
    print("computer wins")
    computer_points = computer_points + 1

elif game == 3 and op == "p":
    print(f"your guess is {game} and computer guess is {op} \n")
    print(f"your point is {human_points} and computer point is {computer_points} \n")
    print("human wins")
    human_points = human_points + 1



number_of_chance = number_of_chance + 1
print(f"{chance - number_of_chance} is left out of {chance} \n")

print("game over")

if human_points > computer_points:
    print("you wins")

elif computer_points > human_points:
    print("computer wins")

else:
    print("tie")

print(f"your point is {human_points} and computer point is {computer_points}")









