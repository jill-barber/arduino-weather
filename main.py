import numpy as np
import os
import asyncio
# from datetime import datetime
# PATH
path = "/home/kali/data_temp/data.txt"

# FUNCTIONS


def cov(string):
    lis = list(string.split(" "))
    while ("" in lis):
        lis.remove("")
    newlis = [float(i) for i in lis]
    return newlis


def avg(l):
    return sum(l) / len(l)


def temprature():
    temprature = os.popen(
        f"cat {path} | grep 'Temp'| grep -Ev '%' | sed 's/[^0-9|.]*//g' | sed 's/$/ /' | tr -d '\n'").read()
    print(temprature)
    list_num_temp = np.array(cov(temprature), dtype=float)
    av_temp = round(avg(list_num_temp), 1)
    return av_temp


def humidity():
    humidity = os.popen(
        f"cat {path} | grep 'Humidity'| tr -d '%' | sed 's/[^0-9|.]*//g' | sed 's/$/ /' | tr -d '\n'").read()
    list_num_humidity = np.array(cov(humidity), dtype=float)
    av_humidity = round(avg(list_num_humidity), 1)
    return av_humidity

# FOR TEMPRATURE

# FOR HUMIDITYs

# print(f"Average Humidity: {av_humidity}\n")
