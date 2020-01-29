# Python Program to find Power of a Number

n = int(input(" Enter a number : "))
p = int(input(" Enter power Value : "))
ans = 1

for i in range(1, p + 1):
    ans = ans * n
print("The result is ",ans)
