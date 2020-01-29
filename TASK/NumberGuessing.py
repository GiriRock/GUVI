import random
def randomno():
  no = random.randint(0,200)
  return no
no = randomno()
for i in range(3):
  guess = int(input("Enter your guess (chances remaining {} )".format(3-i)))
  if(guess==no):
    print("Winner!!!!")
    break
  else:
    if(i==2):
      print("You Lost")
    else:
      print("Try again")
