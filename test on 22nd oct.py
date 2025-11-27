#Create an array with 5 elements, search an element using Binary Search. If the number is found, 
# check if the sum of digits of the number is a prime number or not and display the same.
# If the element is not found, print your roll number and name.

#Add Name and Roll number as file_name for the zip file and upload the same 
#containing python file along with output screenshot

l=[]
for i in range(5):
    x=int(input("enter the element"))
    l.append(x)
l.sort()
print(l)
a=int(input("enter the element to search"))
low=0
high=4
index=-1
while low<=high:
    mid=(low+high)//2
    if a==l[mid]:
        index=mid
        break
    elif a>l[mid]:
        low=mid+1
    elif a<l[mid]:
        high=high-1
if index==-1:
    print("element not present in the array")
    print("Name:Hithesh Rollno: CB.SC.U4CYS24121")
else:
    print("element found at index",index)
    str1=str(a)
    c=0
    for i in str1:
        c=c+int(i)
    print(c)
    count=0
    for i in range(1,c+1):
        if c%i==0:
            count=count+1
    if count==2:
        print("sum of digits is prime")
    else:
        print("sum of digits is not prime")