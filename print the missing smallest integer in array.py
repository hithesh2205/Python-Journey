#Given an unsorted integer array l. Return the smallest positive integer that is not present in l.
l=[]
l1=[]
a=int(input("enter no of elements"))
for i in range(a):
    b=int(input("enter the element to be added"))
    l.append(b)
l.sort()
print(l)
for i in l:
    if i>0:
        l1.append(i)
print(l1)
print("the smallest positive integer that is not present in l is ",l1[0]-1)
