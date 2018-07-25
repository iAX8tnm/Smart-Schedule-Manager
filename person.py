from schedule import Schedule
class Person:
    def __init__(self, personID):
        self.personID = personID
        self.scheduleList = []

    def query_schedule(self, time):
        return True
    
    def delete_schedule(self, time):
        return True

    def add_schedule(self, time, thing):
        schedule = Schedule(time, thing)
        return self.insert_schedule(schedule)

    def add_schedule_without_time(self, thing):
        return True
    
    def get_id(self):
        return self.personID

    def get_scheduleList(self):
        return self.scheduleList

    # 二分查找位置插入
    # #
    def insert_schedule(self, schedule):
        low = 0
        high = len(self.scheduleList) - 1
        while low <= high :
            mid = (low + high) // 2

            if self.scheduleList[mid].compareTo(schedule) == -1:
                low = mid + 1
            elif self.scheduleList[mid].compareTo(schedule) == 1:
                high = mid - 1
            else :
                self.scheduleList.insert(mid, schedule)
                return True #直接跳出
        self.scheduleList.insert(low, schedule)
        return True
