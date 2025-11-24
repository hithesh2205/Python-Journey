hangman=[1,2,3,4,5,6,7]
#hangman 1st stage is the default stage
words=["hithesh",'karthik',"saurabh","yogesh"]
import random
word=random.choice(words)
print(word)
b=len(word)
l=['_']*b
a=len(hangman)-1  #a is max attempts available
count=0
lw=list(word)
print("the len of the word is",b)
print(''.join(l))
while count!=a:
    g=input("enter a alphabet")
    if g in lw:
        print("good guess")
        for i in range(b):
            if lw[i]==g:
                l[i]=g
        print(l)
    else:
        print("wrong")
        count+=1
        print(l)
    if "_" not in l:
        print("you won")
        break
if count==a:
    print("game over")

        
            
    
