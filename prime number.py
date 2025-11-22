n=int(input("enter a num"))
fact=0
for i in range(1,n+1,1):
    if n%i==0:
        fact=fact+1
if fact==2:
    print("prime")
else:
    print("not prime")
