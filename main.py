# -*- coding: utf-8 -*-
from request_nlp import request_nlp
from person import Person
from person import personlist
from datautil import parse_response
from queue import Queue
from gui.talking_window import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import sys
import subprocess
import pickle


#程序用到的shell
CMD_RECORD_5S = "cd temp/ && arecord -d 5 -r 16000 -c 2 -t wav -f S16_LE stereo_ask.wav"
CMD_RECORD_3S = "cd temp/ && arecord -d 3 -r 16000 -c 2 -t wav -f S16_LE stereo_ask.wav"
CMD_STEREO_TO_MONO = "cd temp/ && ffmpeg -i stereo_ask.wav -ac 1 mono_ask.wav"
CMD_MONO_TO_STEREO = "cd temp/ && ffmpeg -i mono_answer.wav -ac 2 stereo_answer.wav"
CMD_PLAY = "cd temp/ && aplay stereo_answer.wav"
CMD_PLAY_NO_PERSON = "cd data/audio/ && aplay dont_know.wav"
CMD_CLEAN = "cd temp/ && rm *"

#程序的状态
WAIT   = 0
RECORD = 1
NLP    = 2
TTS    = 3
PLAY   = 4
state  = WAIT

#当前用户为用户
curUser = None
a = Person("老板")
a.add_schedule("2018-08-09T09:00:00", "出差")
b = Person("经理")
b.add_schedule("2018-08-09TPM", "开会")
c = Person("小李")
c.add_schedule("2018-08-09T09:00:00", "项目")
personlist["老板"] = a
personlist["经理"] = b
personlist["小李"] = c


#全局变量
queue = Queue()
command = None
result = {}
is_shutdown = False
has_no_require_person = False
is_record_short = False
last_require_name = ''


class WorkThread(QThread):
    trigger = pyqtSignal()
    def __init__(self):
        super(WorkThread, self).__init__()
    
    def run(self):
        FSM("小李")
        self.trigger.emit()

class mMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(mMainWindow, self).__init__(parent)
        self.setupUi(self)
    
    def start_record(arg1, arg2):
        global state
        state = RECORD

def close_win():
    qApp = QApplication.instance()
    qApp.quit()

# 录音后网络请求，处理数据
# #
def start_recognition(FILE_PATH):
    global result
    global has_no_require_person
    global is_record_short
    global is_shutdown
    global curUser
    global last_require_name

    r = request_nlp(FILE_PATH, queue)
    if r != None:
        result = parse_response(r, queue)   #应返回intent类型以便调用不同的处理函数
        r = []    #之后r用于接受返回的日程list,再用来显示在屏幕上
        if "intent" in result:

            if result["intent"] == "query_schedule_with_time":                      #查询日程，有时间
                if "time" in result:
                    r = curUser.query_schedule(result["time"])
                    #以后的显示，包括对话，或者日程
            elif result["intent"] == "query_schedule_without_time":                 #查询日程，没时间，在问一次
                is_record_short = True
            elif result["intent"] == "query_add_time":
                if "time" in result:
                    r = curUser.query_schedule(result["time"])


            elif result["intent"] == "add_schedule_with_time":                      #添加日程，有时间
                if "time" in result and "thing" in result:
                    r.append(curUser.add_schedule(result["time"], result["thing"]))
            elif result["intent"] == "add_schedule_without_time":                   #添加日程，没时间，再问一次
                if "thing" in result:
                    curUser.add_schedule_without_time(result["thing"])
                is_record_short = True
            elif result["intent"] == "add_add_time":                                        #获得时间，检查是查询还是添加
                if "time" in result:
                    r.append(curUser.add_time_to_schedule(result["time"]))


            elif result["intent"] == "query_other_schedule_with_time":
                if "name" in result and "time" in result:
                    if result["name"] in personlist:
                        other = personlist[result["name"]]
                        r = other.query_schedule(result["time"])
                    else:
                        has_no_require_person = True
            elif result["intent"] == "query_other_schedule_without_time":
                if "name" in result:
                    if result["name"] in personlist:
                        last_require_name = result["name"]
                        is_record_short = True
                    else :
                        has_no_require_person = True
            elif result["intent"] == "query_other_add_time":
                if "time" in result and last_require_name != '':
                    other = personlist[last_require_name]
                    last_require_name = ''
                    r = other.query_schedule(result["time"])
            elif result["intent"] == "command_shutdown":
                is_shutdown = True
            else :
                pass
        #这之后r是一个有schedule组成的list
        if len(r) != 0:
            result["schedulelist"] = r


def FSM(name):
    global state
    global result
    global is_record_short
    global curUser
    global has_no_require_person
    global personlist

    if name in personlist:
        curUser = personlist[name]
    else :
        print("不好意思，您还没有登陆呢")

    if not os.path.exists("temp"):
        os.mkdir("temp")
    #检查是否有异常退出导致数据没有清理
    if os.path.exists("temp/stereo_ask.wav"):      
        subprocess.Popen(CMD_CLEAN, shell=True)
 #   if os.path.exists("data/personlist.pickle"):
 #       try:
 #           f = open("data/personlist.pickle", "r")
 #           personlist = pickle.load(f)
 #           f.close()
 #       except Exception:
 #           print("恢复信息失败")

    while(True):
        if state == WAIT:
            #input("按回车开始录音：")
            #state = RECORD
            pass

        elif state == RECORD:
            print("start record...")
            #start recording
            if is_record_short :
                subprocess.call(CMD_RECORD_3S, shell=True)
                is_record_short = False
            else :
                subprocess.call(CMD_RECORD_5S, shell=True)
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
                is_tts_done = queue.get()
                if is_tts_done == "TTS_DONE":
                    print("tts done")
                    if has_no_require_person:
                        print("不好意思，我好像不认识他。。。")
                    elif "answer" in result:
                        print(result["answer"])
                        result.pop("answer")
                    if "schedulelist" in result:
                        print("################")
                        if len(result["schedulelist"]) != 0:
                            print("时间：" + result["schedulelist"][0].get_time())
                            print("日程：" + result["schedulelist"][0].get_thing())
                            result.pop("schedulelist")
                        else :
                            print("这个时间还没有日程安排")
                    else :
                            print("这个时间还没有日程安排。")
                    #convert mono to stereo
                    subprocess.call(CMD_MONO_TO_STEREO, shell=True)  
                    state = PLAY
                elif is_tts_done == "TTS_FALSE":
                    state = WAIT
                elif is_tts_done == "NLP_FALSE":
                    state = WAIT

        elif state == PLAY:
            #start playing
            if has_no_require_person:
                has_no_require_person = False
                subprocess.call(CMD_PLAY_NO_PERSON, shell=True)
            else:
                subprocess.call(CMD_PLAY, shell=True)
            print("play done")
            #remove file
            subprocess.Popen(CMD_CLEAN, shell=True)
            if is_shutdown :
#                try:
#                    f = open("data/personlist.pickle", "w")
#                    pickle.dump(personlist, f)
#                    f.close()
#                except Exception:
#                    print("保存信息失败")
                break
            state = WAIT
        else :
            print("something wrong in FSM()")
            state = WAIT




if __name__ == '__main__':

    app = QApplication(sys.argv)
    chat_win = mMainWindow()
    chat_win.btn_record.clicked.connect(chat_win.start_record)

    workThread = WorkThread()
    workThread.start()
    workThread.trigger.connect(close_win)
    chat_win.show()
    
    sys.exit(app.exec_())



