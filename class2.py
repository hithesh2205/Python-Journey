class dog:
    breed="golden retreiver"
    name="chikku"
    def __init__(self):
        print("hello")
    def details(self):
        print("my name is",self.name,"of type",self.breed)
d=dog()
d.details()
#using the 8th line dog() __init__ is triggered
#using the 9th line details() only details() is triggered 
#becoz __init__ is a keyword
#as soon as you create object __init__ is executed