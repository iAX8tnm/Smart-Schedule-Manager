#!/bin/bash
cd audio/
arecord -d 7 -r 16000 -c 2 -t wav -f S16_LE stereo_ask.wav