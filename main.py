from request_nlp import request_nlp
from person import Person
from datautil import parse_response
from queue import Queue
import os
import subprocess


#程序用到的shell
CMD_RECORD_6S = "cd audio/ && arecord -d 6 -r 16000 -c 2 -t wav -f S16_LE stereo_ask.wav"
CMD_RECORD_4S = "cd audio/ && arecord -d 4 -r 16000 -c 2 -t wav -f S16_LE stereo_ask.wav"
CMD_STEREO_TO_MONO = "cd audio/ && ffmpeg -i stereo_ask.wav -ac 1 mono_ask.wav"
CMD_MONO_TO_STEREO = "cd audio/ && ffmpeg -i mono_answer.wav -ac 2 stereo_answer.wav"
CMD_PLAY = "cd audio/ && aplay stereo_answer.wav"
CMD_CLEAN = "cd audio/ && rm *.wav && cd ../json/ && rm result.json"

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
    r = None
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
                curUser.add_schedule(result["time"], result["thing"])
        elif result["intent"] == "add_schedule_without_time":                   #添加日程，没时间，再问一次
            if "thing" in result:
                curUser.add_schedule_without_time(result["thing"])
        elif result["intent"] == "add_add_time":                                        #获得时间，检查是查询还是添加
            if "time" in result:
                curUser.add_time_to_schedule(result["time"])
        else :
            pass
    pass


def FSM():
    global state
    #检查是否有异常退出导致数据没有清理
    if os.path.exists("audio/stereo_ask.wav"):      
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
            start_recognition("audio/mono_ask.wav")
            print("nlp done")
            state = TTS

        elif state == TTS:
            if not queue.empty():
                if queue.get() == "True":
                    print("tts done")
                    if "ask" in result:
                        print(result["ask"])
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
