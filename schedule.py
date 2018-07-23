class Schedule:
    def __init__(self, time, thing):
        self.time = time
        self.thing = thing
    
    def compare(self, time):
        return True

    def get_time(self):
        return self.time
    
    def get_thing(self):
        return self.thing
