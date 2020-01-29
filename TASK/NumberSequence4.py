def sequence():
  st = int(input("Enter the START:"))
  end = int(input("Enter the END:"))
  nos = []
  for i in range(st,end+1):
      nos.append(i**2)
  print(nos)

sequence()
