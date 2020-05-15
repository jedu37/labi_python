import wave
import sys

def main(argv):
    wf = wave.open(argv[1], "rb")
    print(wf.getnchannels())
    print(wf.getframerate())
    print(wf.getsampwidth())
    print(wf.getnframes())

    wf.close()


if __name__ == "__main__":
    main(sys.argv)