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
  print(str(len(list)) + " file(s) founded")
  for wav in list:
    ogg = wav.replace(".wav",".ogg")
    ff = FFmpeg(
    inputs={wav: None},
    outputs={ogg: None})
    ff.run()
    os.remove(wav)
    print(wav + " has been converted.")
else:
    print("No file founded")
print("Convert completed.")


