from webutil import *
from person import Person

p1 = Person(0)

#录音后网络请求，处理数据
r = request_web()   
parse_response(r)   #应返回intent类型以便调用不同的处理函数
