val=input("enter str")
lenval=len(val)
rev=""
for i in range(lenval-1,-1,-1):
    rev=rev+val[i]
if rev==val:
    print("palindrome")
else:
    print("not palindrome")
