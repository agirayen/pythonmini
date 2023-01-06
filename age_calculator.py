

import datetime

def agecalculator(y,m,d):
    today = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    currentage = int((today - dob).days /365.25)
    print(currentage)
agecalculator(1984,11,13)    


   
