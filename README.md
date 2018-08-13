# Smart Schedule Manager
a simple schedule manager implement by using IFLYTEK xfyun platform 

## Hardware Preparation
a Raspberry Pi
a ReSpeaker 2-Mics Pi HAT

## Software Preparation
install 树莓派系统
install 声卡
install ffmpeg
    apt-get install ffmpeg

## 录音指令

arecord -d 10 -r 16000 -c 1 -t wav -f S16_LE test.wav

-d : 录音时间（s）
-r : 频率
-c : 音轨
-t : 文件类型
-f : 格式