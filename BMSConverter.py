import glob
import os
from ffmpy3 import FFmpeg
import sys


def bmsedit(_root_):
    bmspath = _root_ + "*.bms"
    bmepath = _root_ + "*.bme"
    _list_ = glob.glob(bmspath) + glob.glob(bmepath)
    print("Editing...")
    if _list_:
        for bms in _list_:
            print("BMS list:" + bms)
        print(str(len(_list_)) + " BMS file(s) founded.")
        print("Would you like to convert these file(s)?(Y/N)")
        ch1 = input()
        if ch1 == "Y":
            for bms in _list_:
                f = open(bms, 'rb')
                con = f.read().decode(encoding="UTF-8-sig", errors="ignore").replace(".wav", ".ogg")
                f.close()
                f2 = open(bms + "_temp.txt", 'w+')
                f2.write(con)
                f2.close()
                os.remove(bms)
                os.rename(bms + "_temp.txt", bms)
            print("All BMSed have benn edited.")
        else:
            print("Bye.")
    else:
        print("No BMS file(s) founded.")
    choice = input("Do you want to continue? (Y/N): ")
    if choice.lower() == 'N':
        sys.exit(0)


def wavconvert(_root_):
    wavpath = _root_ + "*.wav"
    _list_ = glob.glob(wavpath)
    print("Converting...")
    if _list_:
        print(str(len(_list_)) + " WAV file(s) founded.")
        print("Would you like to convert these file(s)?(Y/N)")
        ch2 = input()
        if ch2 == "Y":
            for wav in _list_:
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
        print("No WAV file founded")
    print("Convert completed.")
    choice = input("Do you want to continue? (Y/N): ")
    if choice.lower() == 'N':
        sys.exit(0)



w = 1
while w:
    print("BMSConverter v0.2")
    print("Please print the path:")
    root = input()
    print("1.Modify BMS file(s)\n2.Convert WAVs to OGGs\n3.Exit")
    num = int(input())
    if num == 1:
        bmsedit(root)
    elif num == 2:
        wavconvert(root)
    elif num == 3:
        break
