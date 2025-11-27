n=int(input("enter the number of elements in the list"))
l=[]
for i in range(n):
    a=int(input("enter the value of each element"))
    l.append(a)
print("unsorted list",l)
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]>=l[j]:
            l[i],l[j]=l[j],l[i]
print("sorted list",l)