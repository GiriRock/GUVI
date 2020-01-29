#reverse the number
a = int(input("enter the number"))
b = str(a)
al = []
for i in b:
  al.append(i)
l = len(al)
for i in range(l-1,-1,-1):
  print(al[i],end="")