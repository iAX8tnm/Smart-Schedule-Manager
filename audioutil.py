from pydub import AudioSegment

def stereo_to_mono():
    stereo = AudioSegment.from_file("audio/stereo_ask.wav")
    mono = stereo.set_channels(1)
    mono.export("audio/mono_ask.wav", format="wav")

def mono_to_stereo():
    mono = AudioSegment.from_file("audio/mono_answer.wav")
    #stereo = mono.set_channels(2)
    stereo = AudioSegment.from_mono_audiosegments(mono, mono)
    stereo.export("audio/stereo_answer.wav")
