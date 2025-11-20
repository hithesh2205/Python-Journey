marks=[]
limit=5
index=-1
print("enter the marks:\n")
for i in range(limit):
    x=int(input())
    marks.append(x)
print(marks)
element=int(input("enter the elmt"))
for i in range(limit):
    if element==marks[i]:
        index=i
if index==-1:
    print("elmt not found")
else:
    print("element found at ",index)