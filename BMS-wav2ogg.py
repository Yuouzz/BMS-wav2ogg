import glob
import os
from ffmpy3 import FFmpeg
state = True
path = ""


def adaptbms(_path_):
    bmspath = _path_ + "*.bms"
    bmepath = _path_ + "*.bme"
    _list_ = glob.glob(bmspath) + glob.glob(bmepath)
    print("Editing...")
    if _list_:
        for bms in _list_:
            print("BMS list:" + bms)
        print(str(len(_list_)) + " BMS file(s) founded.")
        print("Would you like to convert these file(s)?(Y/N)")
        choice1 = input()
        if choice1.lower() == "y":
            for bms in _list_:
                f = open(bms, 'rb')
                con = f.read().decode(encoding="UTF-8-sig", errors="ignore").replace(".wav", ".ogg")
                f.close()
                f_temp = open(bms + "_temp.txt", 'w+')
                f_temp.write(con)
                f_temp.close()
                os.remove(bms)
                os.rename(bms + "_temp.txt", bms)
            print("All BMS file(s) has(ve) been adapted.")
    else:
        print("No BMS file(s) founded.")
    choice2 = input("Do you want to continue? (Y/N): ")
    if choice2.lower() == 'n':
        global state
        state = False


def wavconvert(_path_):
    wavpath = _path_ + "*.wav"
    _list_ = glob.glob(wavpath)
    print("Converting...")
    if _list_:
        print(str(len(_list_)) + " WAV file(s) founded.")
        print("Would you like to convert these file(s)?(Y/N)")
        choice1 = input()
        if choice1.lower() == "y":
            for wav in _list_:
                ogg = wav.replace(".wav", ".ogg")
                ff = FFmpeg(
                  inputs={wav: None},
                  outputs={ogg: None})
                ff.run()
                os.remove(wav)
                print(wav + " has been converted.")
            print("Convert completed.")
    else:
        print("No WAV file founded")
    choice2 = input("Do you want to continue? (Y/N): ")
    if choice2.lower() == 'n':
        global state
        state = False


def pathselect():
    print("Please print the path:")
    _path_ = input()
    return _path_


while state:
    print("BMS-wav2ogg v0.1(https://github.com/Yuouzz/BMS-wav2ogg)")
    if ":" not in path:
        path = pathselect()
    print("1.Adapt BMS file(s)\n2.Convert WAVs to OGGs\n3.Re-select a path\n4.Exit")
    num = int(input())
    if num == 1:
        adaptbms(path)
    elif num == 2:
        wavconvert(path)
    elif num == 3:
        path = pathselect()
    elif num == 4:
        state = False
