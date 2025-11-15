#note that the list should be arranged in acending order
arr=[1,2,11,14,16,24,44,58,61]
n=int(input("enter elmt to search"))
low=0
high=len(arr)-1
index=-1
while low<=high:
    mid = (low+high)//2
    if n==arr[mid]:
        index=mid
        break
    elif n>arr[mid]:
        low=mid+1
    elif n<arr[mid]:
        high=mid-1
if index==-1:
    print("ement not found")
else:
    print(index)
