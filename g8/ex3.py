import wave
import sys
import pyaudio

def main(argv):
    player = pyaudio.PyAudio()
    wf = wave.open(argv[1], "rb")
    print("%s\n Nº de canais: %d\nFreq de Amostra: %d\nTamanho de Amostra: %d\nNº de Frames: %d"%(argv[1],wf.getnchannels(),wf.getframerate(),wf.getsampwidth(),wf.getnframes()))
    
    stream = player.open(format = player.get_format_from_width(wf.getsampwidth()),channels = wf.getnchannels(), rate = wf.getframerate(), output = True)
    
    while True:
        data = wf.readframes(1024)
        if not data:
            break
        stream.write(data)

    stream.close()
    player.terminate()
    wf.close()


if __name__ == "__main__":
    main(sys.argv)