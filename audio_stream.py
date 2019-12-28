import wav
import pyaudio

class Audio_Stream(pyaudio.PyAudio):
    def mic_check(self):
        try:
            get_default_input_device_info()
            return True
        except IOError:
            return False
    def mic_stream(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        if(mic_check):
            return open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
        else:
            print("Check for Audio Input Devices.")
            return null
