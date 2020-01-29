#Sum of prime no till n
st = int(input("Enter the start range(>=1)"))
end = int(input("Enter the end range"))
sump = 0 
for i in range(st,end,1):
  cp = 1
  for j in range(2,i,1):
    if(i%j==0):
      cp = 0
  if(cp==1 and i!=1):
    sump = sump + i
print(sump)