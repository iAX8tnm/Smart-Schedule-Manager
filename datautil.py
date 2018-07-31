#
# a special parse data tool set
# #
import json
import time as T
from request_tts import request_tts
import threading

#
# 保存返回结果，并判断请求时候成功，返回result字典
# #
def parse_response(r):
    result = {}
    f = open('json/result.json','w') #要用try...
    f.write(r)
    f.close()
    j = json.loads(r)
    if j["desc"] == "success":
        result = parse_data(j)
    return result

#
# 粗提取数据并选择下一步对应的操作，返回result字典
# #
def parse_data(j):
    data = j["data"]
    
    result = {}
    for i in data:
        if i["sub"] == "nlp":  #check if is nlp
            j = i["intent"]
            if (len(j) != 0):  #check if this intent is empty
                intent = j
                
                #answer
                answer = intent["answer"]   
                answer = answer["text"]
                result["answer"] = answer       #js写的回答，need to be returned
                #获取到答案之后迅速在另一个线程中请求tts
                task = threading.Thread(target=request_tts, args=(answer,))
                task.start()

                #category
                result["category"]= intent["category"]
                
                semantic = intent["semantic"]
                semantic = semantic[0]

                #intent
                intent = semantic["intent"]  
                result["intent"] = intent

                slots = semantic["slots"]

                #判断意图intent
                if intent == "query_schedule_with_time":         #判断时间，然后显示日程
                    result["time"] = get_time(slots)
                elif intent == "query_schedule_without_time":    #再次提问
                    pass                                    
                elif intent == "add_schedule_with_time":         #直接添加新的日程
                    result["time"] = get_time(slots) 
                    result["thing"] = get_thing(slots)  
                elif intent == "add_schedule_without_time":      #添加只有thing的日程，时间为None,再次提问
                    result["thing"] = get_thing(slots)                         
                elif intent == "time":   
                    result["time"] = get_time(slots)             #返回时间后再根据category判断要执行的操作     
                else:
                    print("something wrong!")
                
                print(answer)
                
    return result


#
# 提取返回结果的time
# 返回时间time为str, 格式有两种，2018-01-01TAM 或2018-01-01T08:00:00
# #
def get_time(slots):
    time = slots[0]    #第0项就是time的语义槽(可能也不是，后期要改)，这里直接提取
    #time
    time = time["normValue"]
    datetime = time[time.index("datetime")+11:time.index("\",\"suggestDatetime")]
    suggestDatetime = time[time.index("suggestDatetime")+18:time.index("\"}")]

    #处理时间格式                               #还有几种编码。。像凌晨，傍晚这些词。。
    n = len(datetime)
    if n == 13:                                #日期带一个上午，一个下午，或者一个晚上的格式
        time = datetime
    elif n == 19:                              #日期带具体时间的形式
        time = datetime
    elif n == 10:                              #只有一个日期，被我在后面加一个TTT伪装成第一种形式
        time = datetime + "TTT"
    elif n == 9:                               #只有一个时间，需要判断，再给他加上个合适的日期
        suggestTime = T.mktime(T.strptime(suggestDatetime,'%Y-%m-%dT%H:%M:%S'))
        curTime = T.time()
        if (suggestTime <= curTime):
            suggestTime = suggestTime + 86400  #加上24h的秒数，获得明天的时间戳
            date = T.strftime("%Y-%m-%d", T.localtime(suggestTime)) #转化成日期字符串
            time = date + datetime
        else :
            time = suggestDatetime
    else :
        print("Ooooooops somthing wrong!")
    
    print(time)#DELETE
    return time

#
# 提取返回结果的thing
# #
def get_thing(slots):  
    thing = None
    for i in slots:
        if i["name"] == "thing":
            thing = i["normValue"]
    return thing
