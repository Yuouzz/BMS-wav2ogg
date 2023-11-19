import glob
import os
from ffmpy3 import FFmpeg

print("Please print the path:")
root = input()
wavpath = root + "*.wav"
bmspath = root + "*.bms"
bmepath = root + "*.bme"
wavlist = glob.glob(wavpath)
bmslist = glob.glob(bmspath) + glob.glob(bmepath)
if wavlist:
    print(str(len(wavlist)) + " file(s) founded.")
    print("Would you like to convert these file(s)?(Y/N)")
    choice = input()
    if choice == "Y":
        for wav in wavlist:
            ogg = wav.replace(".wav", ".ogg")
            ff = FFmpeg(
              inputs={wav: None},
              outputs={ogg: None})
            ff.run()
            os.remove(wav)
            print(wav + " has been converted.")
    else:
        print("Bye.")
else:
    print("No file founded")
print("Convert completed.")

