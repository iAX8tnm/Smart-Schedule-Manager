from schedule import Schedule
import time as T
class Person:
    def __init__(self, personID):
        self.personID = personID
        self.scheduleList = []
        self.no_time_schedule = None

    def query_schedule(self, time):
        if len(time) == 13:                                                          #格式为2018-01-01TAM  , PM,  NI,  TT
            low = 0
            high  = len(self.scheduleList)
            if time[10:] == "TAM":                                                   #返回时间段为00:00:00到12:00:00的日程
                query_timestamp = T.mktime(T.strptime(time,'%Y-%m-%dTAM'))
                low, high = self.get_schedule_range(query_timestamp, 43200)
            elif time[10:] == "TPM":                                                 #返回时间段为12:00:00到18:00:00的日程
                query_timestamp = T.mktime(T.strptime(time,'%Y-%m-%dTPM'))
                low, high = self.get_schedule_range(query_timestamp+43200, 21600)
            elif time[10:] == "TNI":                                                 #返回时间段为18:00:00到24:00:00的日程
                query_timestamp = T.mktime(T.strptime(time,'%Y-%m-%dTNI'))
                low, high = self.get_schedule_range(query_timestamp+64800, 21600)
            elif time[10:] == "TTT":                                                 #返回时间段为00:00:00到24:00:00的日程
                query_timestamp = T.mktime(T.strptime(time,'%Y-%m-%dTTT'))
                low, high = self.get_schedule_range(query_timestamp, 86400)
            return self.scheduleList[low:high]
        elif len(time) == 19:                                                        #格式为2018-01-01T09:00:00
            query_timestamp = T.mktime(T.strptime(time,'%Y-%m-%dT%H:%M:%S'))
            for schedule in self.scheduleList:                                       ##返回时间段为请求时间戳及之后3条日程
                if schedule.get_timestamp() == query_timestamp:
                    i = self.scheduleList.index(schedule)
                    return self.scheduleList[i:i+3]
        else :
            print("Oooooops something wrong!")
        return True
    
    def delete_schedule(self, time):
        return True

    # 添加日程 
    # #
    def add_schedule(self, time, thing):
        schedule = Schedule(time, thing)
        self.insert_schedule(schedule)

    def add_schedule_without_time(self, thing):
        self.no_time_schedule = Schedule(None, thing)

    def add_time_to_schedule(self, time):
        self.no_time_schedule.set_time(time)
        self.insert_schedule(self.no_time_schedule)
        self.no_time_schedule = None
    
    def get_id(self):
        return self.personID

    def get_scheduleList(self):
        return self.scheduleList

    # 二分查找位置插入日程
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

    # 获取时间段的list
    # #
    def get_schedule_range(self, query_timestamp, range):
        low = 0
        high  = len(self.scheduleList)
        range = query_timestamp + range
        for schedule in self.scheduleList:
            if schedule.get_timestamp() >= query_timestamp:
                low = self.scheduleList.index(schedule)
                break
        for schedule in self.scheduleList[::-1]:
            if schedule.get_timestamp() <= range:
                high = self.scheduleList.index(schedule) + 1
                break
        return low, high
