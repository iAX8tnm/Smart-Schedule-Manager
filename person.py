class Person:
    def __init__(self, personID):
        self.personID = personID
        self.scheduleList = []

    def query_schedule(self, time):
        return True
    
    def delete_schedule(self, time):
        return True

    def add_schedule(self, time, thing):
        return True

    def add_schedule_without_time(self, thing):
        return True
    
    def get_id(self):
        return self.personID

    def get_scheduleList(self):
        return self.scheduleList