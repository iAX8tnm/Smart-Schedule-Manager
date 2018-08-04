from request_nlp import request_nlp
from person import Person
from datautil import parse_response
from audioutil import stereo_to_mono
from audioutil import mono_to_stereo
from queue import Queue
import os
import subprocess

#因为讯飞的云函数的技能可能经常变，所以定了接口
QUERY_SERVICE = "MUMUMUSHI.schedule"
ADD_SERVICE = "MUMUMUSHI.set_schedule_2"

queue = Queue()
command = None

WAIT   = 0
RECORD = 1
NLP    = 2
TTS    = 3
PLAY   = 4
state  = WAIT


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
    r = request_nlp(FILE_PATH)
    result = parse_response(r, queue)   #应返回intent类型以便调用不同的处理函数
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
                if result["service"] == QUERY_SERVICE:
                    r = curUser.query_schedule(result["time"])
                elif result["service"] == ADD_SERVICE:
                    curUser.add_time_to_schedule(result["time"])
                else :
                    print("Oooooops something wrong!")
        else :
            print("Oooooops someting wrong!")
    pass


def FSM():
    state  = WAIT
    while(True):
        if state == WAIT:
            command = input("输入s开始录音：")
            state = RECORD
        elif state == RECORD:
            print("start record...")
            subprocess.call("cd audio/ && arecord -d 7 -r 16000 -c 2 -t wav -f S16_LE stereo_ask.wav", shell=True)
            print("record done")
            subprocess.call("cd audio/ && ffmpeg -i stereo_ask.wav -ac 1 mono_ask.wav", shell=True)  
            state = NLP
        elif state == NLP:
            start_recognition("audio/mono_ask.wav")
            print("nlp done")
            state = TTS
        elif state == TTS:
            if not queue.empty():
                if queue.get() == "True":
                    print("tts done")
                    subprocess.check_call("cd audio/ && ffmpeg -i mono_answer.wav -ac 2 stereo_answer.wav", shell=True)  
                    state = PLAY
        elif state == PLAY:
            subprocess.call("cd audio/ && aplay stereo_answer.wav", shell=True)
            print("play done")
            subprocess.call("cd audio/ && rm *.wav && cd ../json/ && rm result.json", shell=True)
            print("clean done")
            state = WAIT
        else :
            print("something wrong")
            state = WAIT

def main():
    while (True):
        command = input("输入s开始录音：")
        print("start record...")
        subprocess.check_call("shell/record.sh", shell=True)
        print("record done")
        stereo_to_mono()
        start_recognition("audio/mono_ask.wav")
        print("nlp done")
        while (queue.empty()):
            pass
        if queue.get() == "True":
            print("tts done")
            mono_to_stereo()
            subprocess.check_call("shell/play.sh", shell=True)
            print("play done")
            subprocess.check_call("shell/clean.sh", shell=True)
            print("clean done")
        else :
            print("Ooooooops something wrong!")

        
FSM()
