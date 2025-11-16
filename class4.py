class student:
    def __init__(self):
        self.name="nothing"
        self.regno="nothing1"
    def display(self):
        print("name",self.name)
        print("regno",self.regno)
s1=student()
s2=student()
s1.name="manoj"
s1.regno="12"
s2.name="hiresh"
s2.regno="13"
s1.display()
s2.display()