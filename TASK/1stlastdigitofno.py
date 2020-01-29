#1st and last digit of a number
a = int(input("enter the number"))
b = str(a)
al = []
for i in b:
  al.append(i)
print("First digit "+al[0])
print("last digit "+al[-1])