l=[]
len=int(input("enter the number of elements"))
for i in range(len):
    a=int(input("enter the element"))
    l.append(a)
for i in l:
    a=0
    for j in str(i):
        
        a=a+int(j)
    print(a)