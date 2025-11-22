n=int(input("enter number for palindrome check"))
num=n
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
if rev==n:
    print("palindrome")
else:
    print("not palindrome")
