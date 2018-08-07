from request_nlp import request_nlp
from person import Person
from datautil import parse_response
from queue import Queue
import os
import subprocess


#程序用到的shell
CMD_RECORD_6S = "cd temp/ && arecord -d 6 -r 16000 -c 2 -t wav -f S16_LE stereo_ask.wav"
CMD_RECORD_4S = "cd temp/ && arecord -d 4 -r 16000 -c 2 -t wav -f S16_LE stereo_ask.wav"
CMD_STEREO_TO_MONO = "cd temp/ && ffmpeg -i stereo_ask.wav -ac 1 mono_ask.wav"
CMD_MONO_TO_STEREO = "cd temp/ && ffmpeg -i mono_answer.wav -ac 2 stereo_answer.wav"
CMD_PLAY = "cd temp/ && aplay stereo_answer.wav"
CMD_CLEAN = "cd temp/ && rm *"

#程序的状态
WAIT   = 0
RECORD = 1
NLP    = 2
TTS    = 3
PLAY   = 4
state  = WAIT

#当前用户为用户0
curUser = Person(0)  

#全局变量
queue = Queue()
command = None
result = {}


# 录音后网络请求，处理数据
# #
def start_recognition(FILE_PATH):
    global result
    r = request_nlp(FILE_PATH)
    result = parse_response(r, queue)   #应返回intent类型以便调用不同的处理函数
    r = []    #之后r用于接受返回的日程list,再用来显示在屏幕上
    if "intent" in result:
        if result["intent"] == "query_schedule_with_time":                      #查询日程，有时间
            if "time" in result:
                r = curUser.query_schedule(result["time"])
                #以后的显示，包括对话，或者日程
        elif result["intent"] == "query_schedule_without_time":                 #查询日程，没时间，在问一次
            pass
        elif result["intent"] == "query_add_time":
            if "time" in result:
                r = curUser.query_schedule(result["time"])

        elif result["intent"] == "add_schedule_with_time":                      #添加日程，有时间
            if "time" in result and "thing" in result:
                r.append(curUser.add_schedule(result["time"], result["thing"]))
        elif result["intent"] == "add_schedule_without_time":                   #添加日程，没时间，再问一次
            if "thing" in result:
                curUser.add_schedule_without_time(result["thing"])
        elif result["intent"] == "add_add_time":                                        #获得时间，检查是查询还是添加
            if "time" in result:
                r.append(curUser.add_time_to_schedule(result["time"]))
        else :
            pass
    #这之后r是一个有schedule组成的list
    result["schedulelist"] = r


def FSM():
    global state
    global result
    #检查是否有异常退出导致数据没有清理
    if os.path.exists("temp/stereo_ask.wav"):      
        subprocess.Popen(CMD_CLEAN, shell=True)
    while(True):
        if state == WAIT:
            input("按回车开始录音：")
            state = RECORD

        elif state == RECORD:
            print("start record...")
            #start recording
            subprocess.call(CMD_RECORD_6S, shell=True)
            print("record done")
            #convert stereo to mono
            subprocess.call(CMD_STEREO_TO_MONO, shell=True)  
            state = NLP

        elif state == NLP:
            start_recognition("temp/mono_ask.wav")
            print("nlp done")
            state = TTS

        elif state == TTS:
            if not queue.empty():
                if queue.get() == "True":
                    print("tts done")
                    if "answer" in result:
                        print(result["answer"])
                        result.pop("answer")
                    if "schedulelist" in result and len(result["schedulelist"]) != 0:
                        print("时间：" + result["schedulelist"][0].get_time())
                        print("日程：" + result["schedulelist"][0].get_thing())
                        result.pop("schedulelist")
                    #convert mono to stereo
                    subprocess.call(CMD_MONO_TO_STEREO, shell=True)  
                    state = PLAY

        elif state == PLAY:
            #start playing
            subprocess.call(CMD_PLAY, shell=True)
            print("play done")
            #remove file
            subprocess.Popen(CMD_CLEAN, shell=True)

            state = WAIT

        else :
            print("something wrong in FSM()")
            state = WAIT

        
FSM()
