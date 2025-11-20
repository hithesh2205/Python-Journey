def prime1(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print("prime")
    else:
        print("not prime")
num=int(input("enter num"))
prime1(num)