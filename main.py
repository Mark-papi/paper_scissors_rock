import random


print ("press 0 for rock, 1 for scissors, 2 for paper/n")
choice = input()

game_rps = ["rock", "scissors", "paper"]
random1 = random.randint(0,2)
if random1 == 0:  
  print (" rock")
  if int(random1)==int(choice):
    print ("its a draw")
  elif int(choice) == 2:
    print ("You won")
  else:
    print ("you lost!!")
elif random1 == 1:
  print ("paper")
else:
  print ("scissors")
