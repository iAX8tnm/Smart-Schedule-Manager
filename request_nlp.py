import requests
import time
import hashlib
import base64


URL = "http://openapi.xfyun.cn/v2/aiui"
APPID = "5b50792b"
API_KEY = "b3aa312944a04778b2c77b71465637b3"
AUE = "raw"
AUTH_ID = "2894c985bf8b1111c6728db79d3479ae"
DATA_TYPE = "audio"
SAMPLE_RATE = "16000"
SCENE = "main"
RESULT_LEVEL = "complete"
LAT = "23.2"
LNG = "116.6"

PERS_PARAM = "{\\\"auth_id\\\":\\\"2894c985bf8b1111c6728db79d3479ae\\\"}"
FILE_PATH = "temp/mono_ask.wav"


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

def request_nlp(queue):
    r = None
    try:
        r = requests.post(URL, headers=buildHeader(), data=readFile(FILE_PATH))
        r = str(r.content, encoding = "utf8")
    except requests.exceptions.RequestException:
        print("网络好像出了点问题")
        queue.put("NLP_FALSE")
    return r
