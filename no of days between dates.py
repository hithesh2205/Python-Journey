import datetime
d1=input("enter date in dd/mm/yyyy format")
d2=input("enter date in dd/mm/yyyy format")
d1=datetime.date(int(d1[6:]),int(d1[3:5]),int(d1[0:2]))
d2=datetime.date(int(d2[6:]),int(d2[3:5]),int(d2[0:2]))
diff=(d2-d1).days-1
print(diff)