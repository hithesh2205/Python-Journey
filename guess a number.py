import random
num=random.randint(1,20)
print(num)
attempts=5
while attempts>0:
    try:
        g=int(input("enter the number"))
        if g==num:
            print("correct")
            break
        elif g>num:
            print("too high")
        else:
            print("too low")
        attempts=attempts-1
        print("you have ",attempts,"more")
    except ValueError:
        print("enter a valid input")
if attempts==0:
    print("game over")
    print("the number was",num)
        
            
        