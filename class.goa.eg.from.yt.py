# ram likes party , sam likes only beach
class goa:
    print("hello")
    name=''
    drink=''
    def party(self):
        print("Hi i am ram,i like to party")
    def beach(self):
        print("hi i am sam, i enjoy beach")
ram=goa() # lines 7 and 8 gives access to ram and sam to goa
sam=goa()  #here goa is class/blueprint and sam , ram are objects
ram.name="ram"  
ram.drink='yes'         
sam.name="sam"
sam.drink='no'
print(ram.name)
print('drink',ram.drink)
ram.party()
print(sam.name)
print('drink',sam.drink)
sam.beach()
#if you delete line 10 to line 21 also hello is being printed
