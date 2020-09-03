#import datetime
#d = int(input("d"))
#m = int(input("m"))
#y = int(input("y"))
#try:
    #data = datetime.date(y, m, d)
    #print(data)
    #print("True")
#except:
   # print("False")

from datetime import date

class Date():
    def __init__(self):
        pass
    def testdate(self, d, m, y):
        input_date = str(y) + str(m) + str(d)

    try:
        date(y, m, d)
        print(str(input_date) + "True")
        return True

    except:
        print(str(input_date) + "False")
        return False

