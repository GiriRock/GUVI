import random
def randomno():
  no = random.randint(1,3)
  return no
def display(no,guess):
  if(no == 1 and guess ==3):
    print("Computer WON!")
  elif(no == 2 and guess == 1):
    print("U WON!")
  elif(no ==3 and guess == 1):
    print("U WON!")
  elif(no==1 and guess==2):
    print("Computer WON!")
  elif(no==3 and guess==2):
    print("Computer WON!")
  elif(no == 2 and guess == 3):
    print("U WON!")
ch='y'
while(ch=='y' or ch=='Y'):
  no = randomno()
  print("1.ROCK")
  print("2.PAPER")
  print("3.SCISSOR")
  guess = int(input("Enter your choice: "))
  if(no == guess):
    print("DRAW!!")
  else:
    display(no,guess)
  ch = input("Do u want to continue(y/n)")