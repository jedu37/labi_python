import wave
import struct
import sys
from struct import pack
import math

def copy(data):
    output = []
    for index,value in enumerate(data):
        output.append(value)
    
    return output

def reverse(data):
    output = []
    for index,value in enumerate(data):
        output.append(value)
    
    output.reverse()

    return output

def volume(data,val):
    output = []
    for index,value in enumerate(data):
        output.append(value*val)

    return output

def main(argv):
    stream = wave.open(argv[1], "rb")

    sample_rate = stream.getframerate()
    
    num_frames = stream.getnframes()
    
    raw_data = stream.readframes( num_frames )
    
    stream.close()
    
    data = struct.unpack("%dh" % num_frames, raw_data) # "B" para ficheiros 8bits
    
    # Aplica efeito sobre data, para output_data
    i = 2
    output_data = []
    while i < len(argv):
        if argv[i] == "copy":
            output_data = copy(data)
        
        #elif argv[i] == "foo":
            #param = int(argv[i+1])
            #output_data = foo(data, param)
        
        elif argv[i] == "reverse":
            output_data = reverse(data)
        
        elif argv[i] == "volume":
            output_data = volume(data, float(argv[i+1]))
        
        i += 1

    wvData = b""
    
    name = argv[1][15:]

    for v in output_data:
        wvData += pack("h", int(v))
        stream = wave.open("g8/sound_files/out-"+name, "wb")
        stream.setnchannels(1)
        stream.setsampwidth(2)
        stream.setframerate(sample_rate)
        stream.setnframes(len(wvData))
        stream.writeframes(bytearray(wvData))
    
    stream.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: %s wave-file filter1 <params> filter2 <params> ..." % sys.argv[0])
    else:
        main(sys.argv)
