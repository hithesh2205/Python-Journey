class lap:
    def __init__(self):
        self.ram=''
        self.price=0
    def display(self):
        print("ram",self.ram)
        print("price",self.price)
hp=lap()
dell=lap()
dell.ram='16gb'
dell.price=85000
hp.ram="8gb"
hp.price=55000
hp.display()
print("hello")
dell.display()
#from this we can see that self is the current object called
#when hp object is called in the 14th line it prints hp details that is there it is not self.ram it is hp.ram
#then it prints hello
#then it prints dell details that it is dell.ram and dell.price instead of self