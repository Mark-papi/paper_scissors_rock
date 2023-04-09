
import random


print ("press 0 for rock, 1 for scissors, 2 for paper/n")
choice = input()

game_rps = ["rock", "scissors", "paper"]
random1 = random.randint(0,2)
if random1 == 0:  
  print (" computer chose rock")
  if int(random1)==int(choice):
    print ("its a draw")
  elif int(choice) == 2:
    print ("You won")
  else:
    print ("you lost!!")
elif random1 == 1:
  print ("computer chose scissors")
  if int(random1)==int(choice):
    print ("its a draw")
  elif int(choice)== 1:
    print ('You won!!')
  else:
    print ("you lost!")
else:
  print ("computer chose paper")
  if int(random1) == int(choice):
    print ("its a draw")
  elif int(choice) == 0:
    print ("you won!")
  else:
    print (" you lost!!")


















