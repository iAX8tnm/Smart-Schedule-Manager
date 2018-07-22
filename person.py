class Person:
    def __init__(self, personID):
        self.personID = personID
        self.scheduleList = []

    def ret_id(self):
        return self.personID

    def query_schedule(self, time):
        return True
    
    def delete_schedule(self, time):
        return True

    def add_schedule(self, time, event):
        return True
