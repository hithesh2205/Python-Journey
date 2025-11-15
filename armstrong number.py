#armstrong number
#sum of individual digit with power to number of digits
# eg 153 3^3+5^3+1^3
n=int(input("enter num"))
a=str(n)
b=len(a)
res=0
for i in a:
    res=res+(int(i)**b)
if n==res:
    print("armstrong")
else:
    print("not armstrong")
