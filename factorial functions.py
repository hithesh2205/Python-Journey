def fact(num):
    f=1
    while (num):
        f*=num
        num-=1
    print(f)
n=int(input("enter a num"))
fact(n)