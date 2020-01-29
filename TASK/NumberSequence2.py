def sequence():
  st = int(input("Enter the START:"))
  end = int(input("Enter the END:"))
  nos = []
  for i in range(st,end+1):
    if(i%2!=0):
      nos.append(i)
  print(nos)

sequence()
