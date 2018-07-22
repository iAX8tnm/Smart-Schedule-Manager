import requests
import time
import hashlib
import base64
import json

URL = "http://openapi.xfyun.cn/v2/aiui"
APPID = "5b50792b"
API_KEY = "b3aa312944a04778b2c77b71465637b3"
AUE = "raw"
AUTH_ID = "2894c985bf8b1111c6728db79d3479ae"
DATA_TYPE = "audio"
SAMPLE_RATE = "16000"
SCENE = "main"
RESULT_LEVEL = "complete"
LAT = "39.938838"
LNG = "116.368624"

PERS_PARAM = "{\\\"auth_id\\\":\\\"2894c985bf8b1111c6728db79d3479ae\\\"}"
FILE_PATH = "audio/test.wav"


def buildHeader():
    curTime = str(int(time.time()))
    param = "{\"result_level\":\""+RESULT_LEVEL+"\",\"auth_id\":\""+AUTH_ID+"\",\"data_type\":\""+DATA_TYPE+"\",\"sample_rate\":\""+SAMPLE_RATE+"\",\"scene\":\""+SCENE+"\",\"lat\":\""+LAT+"\",\"lng\":\""+LNG+"\"}"
    paramBase64 = base64.b64encode(bytes(param, encoding = "utf8"))

    m2 = hashlib.md5()
    m2.update((API_KEY + curTime + str(paramBase64, encoding = "utf8")).encode("utf-8"))
    checkSum = m2.hexdigest()

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
    }
    return header

def readFile(filePath):
    binfile = open(filePath, 'rb')
    data = binfile.read()
    return data

def request_web():
    r = requests.post(URL, headers=buildHeader(), data=readFile(FILE_PATH))
    r = str(r.content, encoding = "utf8")
    return r

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
                semantic = intent["semantic"]
                semantic = semantic[0]
                slots = semantic["slots"]
                time = slots[0]
                time_norm_value = time["normValue"]
                print(time_norm_value)
            