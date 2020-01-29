#sum of odd numbers
st = int(input("Enter the start range(>=1)"))
end = int(input("Enter the end range"))
sumn = 0 
for i in range(st,end,1):
  if(i % 2 != 0):
    sumn = sumn + i
print(sumn)