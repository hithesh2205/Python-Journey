
def add(num):
    if num==1:
        sum=1
    else:
        sum=num+add(num-1)
    return sum
num=int(input("enter the num"))
a=add(num)
print(a)
