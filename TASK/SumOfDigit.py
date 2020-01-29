# Python Program to find Sum of Digits of a Number using While Loop

n = int(input("Enter the no: "))
Sum = 0

while(n > 0):
    r = n % 10
    Sum = Sum + r
    n = n //10

print("sum= ",Sum)
