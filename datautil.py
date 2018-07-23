#
# a special parse data tool set
# #
import json


def parse_response(r):
    f = open('json/result.json','w')
    f.write(r)
    f.close()
    j = json.loads(r)
    if j["desc"] == "success":
        parse_data(j)

def parse_data(j):
    data = j["data"]
    #this "data" is a list, we need to check 
    #which list item is we want
    for i in data:
        if i["sub"] == "nlp":  #check if is nlp
            j = i["intent"]
            if (len(j) != 0):  #check if this intent is empty
                intent = j
                
                #sessionIsEnd
                sessionIsEnd = intent["sessionIsEnd"]  #need to be returned
                
                #answer
                answer = intent["answer"]   
                answer = answer["text"]  #js写的回答，need to be returned

                semantic = intent["semantic"]
                semantic = semantic[0]

                #intent
                intent = semantic["intent"]  #这个是具体的intent，need to be returned 

                slots = semantic["slots"]

                #大概从住这里开始封装不同意图具体的处理函数
                time = slots[0]    #第零项就是time的语义槽(可能也不是，后期要改)，这里直接提取
                #time
                time = time["normValue"]
                datetime = time[time.index("datetime"):time.index(",\"suggestDatetime")]
                suggestDatetime = time[time.index("suggestDatetime"):time.index("}")]
                print(datetime)   #提取出来的两个时间
                print(suggestDatetime)   #need to be returned

               
    return 


#最重要的是什么？answer_text，具体的intent，sessionIsEnd
#answer_text用于返回去显示或者读出来
#intent才知道当前录音的意图是什么
#sessionIsEnd才知道当前对话时候已经结束，但是假设我已经知道了intent的话，我是可以知道是否还需要继续对话的，所以，可以把他们一起判断
#但根据我们的intent，我们才知道要怎么提取数据，所以，根据不同的intent，调用不同的具体的处理函数~(￣▽￣)~*