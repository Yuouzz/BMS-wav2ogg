import glob
import os
import subprocess
import configparser

state = True
path = ""


def bms_adapt(_path_):
    if os.path.exists("config.ini"):
        config = configparser.ConfigParser()
        config.read("config.ini")
        _input_format_ = config_read(config, 'convert', 'input_format')
        _output_format_ = config_read(config, 'convert', 'output_format')
    else:
        _input_format_ = "None"
        _output_format_ = "None"
    # Read config
    bms_path = _path_ + "*.bms"
    bme_path = _path_ + "*.bme"
    _list_ = glob.glob(bms_path) + glob.glob(bme_path)
    print("Editing...")
    if _list_:
        for bmx in _list_:
            print("BMS list:" + bmx)
        print(str(len(_list_)) + " BMS file(s) founded.")
        print("Would you like to convert these file(s)?(Y/N)")
        choice_convert = input()
        if choice_convert.lower() == "y":
            for bmx in _list_:
                _f_ = open(bmx, 'rb')
                con = _f_.read().decode(encoding="UTF-8-sig", errors="ignore").replace(_input_format_, _output_format_)
                _f_.close()
                f_temp = open(bmx + "_temp.txt", 'w+')
                f_temp.write(con)
                f_temp.close()
                os.remove(bmx)
                os.rename(bmx + "_temp.txt", bmx)
            print("All BMS(es) has(ve) been adapted.")
    else:
        print("No BMS file(s) founded.")
    choice_continue = input("Do you want to continue? (Y/N): ")
    if choice_continue.lower() == 'n':
        global state
        state = False


def convert(_path_):
    if os.path.exists("config.ini"):
        config = configparser.ConfigParser()
        config.read("config.ini")
        _input_format_ = config_read(config, 'convert', 'input_format')
        _output_format_ = config_read(config, 'convert', 'output_format')
        _channels_ = config_read(config, 'convert', 'channels')
        _frequency_ = config_read(config, 'convert', 'frequency')
        _ffmpeg_path_ = config_read(config, 'convert', 'ffmpeg_path')
    else:
        _input_format_ = "None"
        _output_format_ = "None"
        _channels_ = "None"
        _frequency_ = "None"
        _ffmpeg_path_ = "None"
    # Read config.
    if _input_format_ and not _input_format_ == "None":
        input_file = _path_ + "*." + _input_format_
    else:
        input_file = _path_ + "*.wav"
    _list_ = glob.glob(input_file)
    # Get input file(s) list.
    if _ffmpeg_path_ and not _ffmpeg_path_ == "None":
        subprocess.run(_ffmpeg_path_)
    print("Converting...")
    if _list_:
        print(str(len(_list_)) + " sound file(s) founded.\nWould you like to convert these file(s)?(Y/N)")
        choice_convert = input()
        if choice_convert.lower() == "y":
            for _input_file_ in _list_:
                if not _input_format_ or _input_format_ == "None":
                    _input_format_ = "wav"
                if not _output_format_ or _output_format_ == "None":
                    _output_format_ = "ogg"
                _output_file_ = _input_file_.replace("." + _input_format_, "." + _output_format_)
                cmd = "ffmpeg -i " + _input_file_
                if _channels_ and not _channels_ == "None":
                    cmd += " -ac " + _channels_
                if _frequency_ and not _frequency_ == "None":
                    cmd += " -ar " + _frequency_
                cmd += " " + _output_file_
                subprocess.run(cmd)
                os.remove(_input_file_)
                print(_input_file_ + " has been converted.")
            print("Convert completed.")
    else:
        print("No WAV file founded")
    choice_continue = input("Do you want to continue? (Y/N): ")
    if choice_continue.lower() == 'n':
        global state
        state = False


def path_select():
    print("Please print the path:")
    _path_ = input()
    return _path_


def settings():
    if not os.path.exists("config.ini"):
        _f_ = open("config.ini", "w")
        _f_.close()
    _state_ = True
    _config_ = configparser.ConfigParser()
    _config_.read("config.ini")
    _config_temp_ = _config_
    while _state_:
        print("-Settings-\n1.Convert settings\n2.Exit")
        choice = int(input())
        if choice == 1:
            _config_convert_ = {'input_format': config_read(_config_, 'convert', 'input_format'),
                                'output_format': config_read(_config_, 'convert', 'output_format'),
                                'channels': config_read(_config_, 'convert', 'channels'),
                                'frequency': config_read(_config_, 'convert', 'frequency'),
                                'ffmpeg_path': config_read(_config_, 'convert', 'ffmpeg_path')}
            _config_temp_['convert'] = settings_convert(_config_convert_)
        if choice == 2:
            _state_ = False
    _f_ = open("config.ini", "w+")
    _config_.write(_f_)
    _f_.close()


def settings_convert(_configdict_):
    _state_ = True
    while _state_:
        print("Current settings:")
        print(_configdict_)
        print("1.Edit input format\n"
              "2.Edit output format\n"
              "3.Edit channels\n"
              "4.Edit frequency\n"
              "5.Clear settings\n"
              "6.Select FFmpeg path\n"
              "7.Exit")
        choice = int(input())
        if choice == 1:
            print("Please print the input format:(Example:wav)")
            _configdict_['input_format'] = str(input())
        if choice == 2:
            print("Please print the output format:")
            _configdict_['output_format'] = str(input())
        if choice == 3:
            print("Please print the channels:")
            try:
                _configdict_['channels'] = str(int(input()))
            except ValueError:
                print("Error:Please print a valid number.")
        if choice == 4:
            print("Please print the frequency:")
            try:
                _configdict_['frequency'] = str(int(input()))
            except ValueError:
                print("Error:Please print a valid number.")
        if choice == 5:
            for _i_ in _configdict_:
                _i_ = "None"
        if choice == 6:
            print("Please print FFmpeg path:")
            _configdict_['ffmpeg_path'] = str(input())
        if choice == 7:
            _state_ = False
    return _configdict_


def config_read(_config_, _section_, _option_):
    if _config_.has_option(_section_, _option_):
        return _config_.get(_section_, _option_)
    else:
        return "None"


while state:
    print("BMS-wav2ogg v0.1 (github.com/Yuouzz/BMS-wav2ogg)")
    if not path:
        path = path_select()
    print("-Main menu-\n1.Adapt BMS file(s)(Testing)\n2.Convert sound file(s)\n3.Re-select a path\n4.Settings\n5.Exit")
    num = int(input())
    if num == 1:
        bms_adapt(path)
    elif num == 2:
        convert(path)
    elif num == 3:
        path = path_select()
    elif num == 4:
        settings()
    elif num == 5:
        state = False
