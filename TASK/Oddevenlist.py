#sum of odd and even elements in the list
a = list(input("Enter the List"))
odd = []
even = []
sume = 0
sumo = 0
for i in range(0, len(a)): 
    a[i] = int(a[i])
for i in a:
  if(i % 2 ==0):
    even.append(i)
  else:
    odd.append(i)
for j in odd:
  sumo = sumo + j 
for k in even:
  intk = int(k)
  sume = sume + k 
print(sumo)
print(sume)