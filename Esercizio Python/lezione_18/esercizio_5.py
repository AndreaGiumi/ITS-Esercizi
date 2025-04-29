import datetime
class DatabaseDates:
    def __init__(self, date):
        self.date = date

    def addData(self):
        self.date = datetime("%d/%m/%Y")



s = datetime.datetime.now()



print(s.strftime("%d/%m/%Y"))