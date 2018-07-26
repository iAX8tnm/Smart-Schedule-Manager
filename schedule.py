import time as T

class Schedule:
    def __init__(self, time, thing):
        self.time = time
        self.thing = thing
        self.timestamp = None
        if len(time) == 13:                         #格式为2018-01-01TAM  , PM,  NI,  TT
            if time[10:] == "TAM":
                self.timestamp = T.mktime(T.strptime(time,'%Y-%m-%dTAM')) + 21600
            elif time[10:] == "TPM":
                self.timestamp = T.mktime(T.strptime(time,'%Y-%m-%dTPM')) + 46800
            elif time[10:] == "TNI":
                self.timestamp = T.mktime(T.strptime(time,'%Y-%m-%dTNI')) + 72000
            elif time[10:] == "TTT":
                self.timestamp = T.mktime(T.strptime(time,'%Y-%m-%dTTT')) + 21600
        elif len(time) == 19:                       #格式为2018-01-01T09:00:00
            self.timestamp = T.mktime(T.strptime(time,'%Y-%m-%dT%H:%M:%S'))
        else :
            print("Oooooops something wrong!")
         
    
    def compare(self, time):
        return True

    def get_time(self):
        return self.time

    def get_timestamp(self):
        return self.timestamp
    
    def get_thing(self):
        return self.thing


    #       主要是比较时间戳！
    #       
    #       另外，由于querry_schedule要返回的是一个范围时间的日程（不同与添加，即使说是下午但是人可以 指定为13点钟提醒）
    #       所以，这个函数应该用datetime判断
    # #
    def compareTo(self, that):
        if self.get_timestamp() < that.get_timestamp():
            return -1
        elif self.get_timestamp() > that.get_timestamp():
            return 1
        return 0