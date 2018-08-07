#-*- coding: utf-8 -*-
import requests
import re
import time
import hashlib
import base64
import struct

URL = "http://api.xfyun.cn/v1/service/v1/tts"
AUE = "raw"
APPID = "5b50792b"
API_KEY = "7097a8f950b5714a1f1d0510664fcbdf"

def getHeader():
        curTime = str(int(time.time()))
        param = "{\"aue\":\""+AUE+"\",\"auf\":\"audio/L16;rate=16000\",\"voice_name\":\"xiaoyan\",\"engine_type\":\"intp65\"}"
        paramBase64 = base64.b64encode(bytes(param, encoding = "utf8"))
        m2 = hashlib.md5()
        m2.update((API_KEY + curTime + str(paramBase64, encoding = "utf8")).encode("utf-8"))
        checkSum = m2.hexdigest()
        header ={
                'X-CurTime':curTime,
                'X-Param':paramBase64,
                'X-Appid':APPID,
                'X-CheckSum':checkSum,
                'X-Real-Ip':'127.0.0.1',
                'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',
        }
        return header

def getBody(text):
        data = {'text':text}
        return data

def writeFile(file, content):
    with open(file, 'wb') as f:
        f.write(content)
    f.close()


# 供外部调用把参数text转成语音，并存在audio/下， 以返回的sid作为文件名
# #
def request_tts(text, queue):
    r = requests.post(URL,headers=getHeader(),data=getBody(text))
    contentType = r.headers['Content-Type']
    if contentType == "audio/mpeg":
        writeFile("audio/mono_answer.wav", r.content)
        queue.put("True")
    else :
        print(r.text)
        queue.put("False")

def request_tts_no_queue(text):
    r = requests.post(URL,headers=getHeader(),data=getBody(text))
    contentType = r.headers['Content-Type']
    if contentType == "audio/mpeg":
        writeFile("audio/mono_answer.wav", r.content)
    else :
        print(r.text)

request_tts_no_queue("正在启动自毁程序！5，4，3，2，1，bang!")