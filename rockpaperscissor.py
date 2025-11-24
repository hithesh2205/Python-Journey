import random
action=['rock','paper','scissor']
a=random.choice(action)
print(a)
choice=input("enter your action")
if choice==a:
    print("its a tie")
elif (choice=='rock'and a=='scissor') or (choice=='paper'and a=='rock') or (choice=='scissor'and a=='paper'):
    print("you win")
else:
    print("computer wins")