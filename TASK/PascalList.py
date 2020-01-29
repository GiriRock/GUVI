def pattern():
  n = int(input("Enter the Range"))
  listp = [1]
  print(listp) 
  for i in range(2,n+1):
    listp = [1]
    for j in range(2,i):
      listp.append(j)
    for k in range(i,0,-1):
      listp.append(k)
    print(listp)
pattern()