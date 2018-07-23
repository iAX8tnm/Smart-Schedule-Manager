#
# a special parse data tool set
# #
import json

#
# 保存返回结果，并判断请求时候成功
# #
def parse_response(r):
    f = open('json/result.json','w') #要用try...
    f.write(r)
    f.close()
    j = json.loads(r)
    if j["desc"] == "success":
        parse_data(j)

#
# 粗提取数据并选择下一步对应的操作
# #
def parse_data(j):
    data = j["data"]
    
    for i in data:
        if i["sub"] == "nlp":  #check if is nlp
            j = i["intent"]
            if (len(j) != 0):  #check if this intent is empty
                intent = j
                
                #category
                category = intent["category"]
                #answer
                answer = intent["answer"]   
                answer = answer["text"]         #js写的回答，need to be returned

                semantic = intent["semantic"]
                semantic = semantic[0]

                #intent
                intent = semantic["intent"]  

                slots = semantic["slots"]

                #判断意图intent
                if intent == "query_schedule_with_time":         #判断时间，然后显示日程
                    get_time(slots)
                elif intent == "query_schedule_without_time":    #再次提问
                    get_time(slots)                                    
                elif intent == "add_schedule_with_time":         #直接添加新的日程
                    get_time(slots)   
                elif intent == "add_schedule_without_time":      #添加只有thing的日程，时间为None,再次提问
                    thing = get_thing(slots)                           
                elif intent == "time":   
                    if category == "MUMUMUSHI.schedule":         #判断时间，然后显示日程
                        get_time(slots)
                    elif category == "MUMUMUSHI.set_schedule_2": #找到上次那个只有thing的日程，加上时间
                        get_time(slots)
                else:
                    print("something wrong!")
                
                print(answer)


#
# 提取返回结果的time
# #
def get_time(slots):
    time = slots[0]    #第0项就是time的语义槽(可能也不是，后期要改)，这里直接提取
    #time
    time = time["normValue"]
    datetime = time[time.index("datetime"):time.index(",\"suggestDatetime")]
    suggestDatetime = time[time.index("suggestDatetime"):time.index("}")]
    #print(datetime)       
    #print(suggestDatetime)   
    return datetime, suggestDatetime

#
# 提取返回结果的thing
# #
def get_thing(slots):  
    thing = None
    for i in slots:
        if i["name"] == "thing":
            thing = i["normValue"]
    return thing

#
# 比较为字符串的时间，因为实在是没有办法，询问日程，添加日程都可能只是说一个时间段而不是那个钟点
# 假如为Schedule类添加一个index的话，在添加插入类的日程就要全改后面的数据，所以很不方便
# 考虑直接字符串比较，并且采用二分查找
#       根据当前请求的time，与scheduleList中间项的time比较
#       if querry.time > meddle.time:
#           first = meddle
#       elif querry.time == meddle.time:
#           return meddle+1
#       elif querry.time < meddle.time:
#           last = meddle
#       ......
#       主要是比较字符串吧
#       
#       另外，由于querry_schedule要返回的是一个范围时间的日程（不同与添加，即使说是下午但是人可以 指定为13点钟提醒）
#       所以，这个函数应该用datetime判断
# #
def compare_time():
    return True
