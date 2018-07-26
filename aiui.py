from webutil import request_web
from person import Person
from datautil import parse_response
#因为讯飞的云函数的技能可能经常变，所以定了接口
QUERY_CATEGORY = "MUMUMUSHI.schedule"
ADD_CATEGORY = "MUMUMUSHI.set_schedule_2"


curUser = Person(0)  #0号人物为当前用户

#test
curUser.add_schedule("2018-07-27TPM", "项目")
curUser.add_schedule("2018-07-27TTT", "睡觉")
curUser.add_schedule("2018-07-28TAM", "拿快递")
curUser.add_schedule("2018-07-28T18:00:00", "学习")
curUser.add_schedule("2018-07-29T07:00:00", "写作业")
curUser.add_schedule("2018-08-01T12:30:00", "去买东西")

# 录音后网络请求，处理数据
# #
def start_recognition(FILE_PATH):
    r = request_web(FILE_PATH)
    result = parse_response(r)   #应返回intent类型以便调用不同的处理函数
    r = None
    if "intent" in result:
        if result["intent"] == "query_schedule_with_time":                      #查询日程，有时间
            if "time" in result:
                r = curUser.query_schedule(result["time"])
        elif result["intent"] == "query_schedule_without_time":                 #查询日程，没时间，在问一次
            start_recognition("audio/time2.wav")
        elif result["intent"] == "add_schedule_with_time":                      #添加日程，有时间
            if "time" in result and "thing" in result:
                curUser.add_schedule(result["time"], result["thing"])
        elif result["intent"] == "add_schedule_without_time":                   #添加日程，没时间，再问一次
            if "thing" in result:
                curUser.add_schedule_without_time(result["thing"])
                start_recognition("audio/time2.wav")
        elif result["intent"] == "time":                                        #获得时间，检查是查询还是添加
            if "time" in result:
                if result["category"] == QUERY_CATEGORY:
                    r = curUser.query_schedule(result["time"])
                elif result["category"] == ADD_CATEGORY:
                    curUser.add_time_to_schedule(result["time"])
                else :
                    print("Oooooops something wrong!")
        else :
            print("Oooooops someting wrong!")
    pass

start_recognition("audio/query_schedule_without_time.wav")