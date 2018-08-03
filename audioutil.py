from pydub import AudioSegment

def stereo_to_mono():
    stereo = AudioSegment.from_file("audio/src.wav")
    mono = stereo.set_channels(1)
    mono.export("audio/src.wav", format="wav")

def mono_to_stereo():
    mono = AudioSegment.from_file("audio/answer.wav")
    stereo = mono.set_channels(2)
    stereo.export("audio/answer.wav")
