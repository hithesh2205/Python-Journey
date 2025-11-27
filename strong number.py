n=int(input("enter your number"))
sum=0
num=n
while n>0:
    rem=n%10
    fact=1
    while rem>0:
        fact=fact*rem
        rem=rem-1
    sum=sum+fact
    n=n//10
if sum==num:
    print("strong number")
else:
    print("not strong number")
    