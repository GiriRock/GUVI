#Write a program to calculate product of digits of a number

n = int(input("Enter the no: "))
pro = 1

while(n > 0):
    r = n % 10
    pro = pro * r
    n = n //10

print("product= ",pro)
