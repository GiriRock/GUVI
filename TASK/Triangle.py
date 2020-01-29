def pattern():
  n = int(input("Enter the Range"))
  for i in range(1,n+1):
    for l in range(i,n):
      print(" ",end=" ")
    for j in range(1,i):
      print(j,end=" ")
    for k in range(i,0,-1):
      print(k,end=" ")
    print()
pattern()