#sum of all factors of num except num is the same num eg:28 1,2,4,7,14
n=int(input("enter the number"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")