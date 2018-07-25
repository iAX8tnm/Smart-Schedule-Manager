from webutil import request_web
from person import Person
from datautil import parse_response

curUser = Person(0)  #0号人物为当前用户

# 录音后网络请求，处理数据
# #
def start_recognition():
    r = request_web()   
    result = parse_response(r)   #应返回intent类型以便调用不同的处理函数
    if "intent" in result:
        if result["intent"] == "query_schedule_with_time":                      #查询日程，有时间
            if "time" in result:
                curUser.query_schedule(result["time"])
        elif result["intent"] == "query_schedule_without_time":                 #查询日程，没时间，在问一次
            pass
        elif result["intent"] == "add_schedule_with_time":                      #添加日程，有时间
            if "time" in result and "thing" in result:
                curUser.add_schedule(result["time"], result["thing"])
        elif result["intent"] == "add_schedule_without_time":                   #添加日程，没时间，再问一次
            pass
        elif result["intent"] == "time":                                        #获得时间，检查是查询还是添加
            pass
        else :
            print("Oooooops someting wrong!")

start_recognition()