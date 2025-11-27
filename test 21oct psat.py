l=eval(input("enter the list of elements"))
l.sort()
a=int(input("enter the element to search"))
low=0
high=len(l)-1
index=-1
while low<=high:
    mid=(low+high)//2
    if a==l[mid]:
        index=mid
        break
    elif a>l[mid]:
        low=mid+1
    else:
        high=mid-1
if index==-1:
    print("element not found")
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum=sum+i
    if a==sum:
        print("perfect number")
    else:
        print("not a perfect number")                       
else:
    print("element found at index",index)
    sum1=0
    for i in str(a):
        fact=1
        b=int(i)
        while b>0:
            fact=fact*b
            b=b-1
        sum1=sum1+fact
    if sum1==a:
        print("strong")
    else:
        print("weak")
        
