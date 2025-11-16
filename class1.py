class NewClass:
    def __init__(self,num):
        self.x=num
    def sq(self):
        return self.x * self.x
c2=NewClass(10)
print(c2.sq())
