import datetime
d=int(input("d"))
m=int(input("m"))
y=int(input("y"))
try:
    data = datetime.date(y, m, d)
    print(data)
    print("True")
except:
    print("False")
