#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 02
# Problem 4
# 204111 Sec 003

mls=int(input("Input number of milliseconds: "))
day=mls/(1000*24*60*60)
mls=mls%(1000*24*60*60)
hour=mls/(1000*60*60)
mls=mls%(1000*60*60)
min=mls/(1000*60)
mls=mls%(1000*60)
sec=mls/1000
mls=mls%(1000)
print("Results = %d day(s), %d hour(s), %d minute(s), %d second(s), and %d millisec(s) "%(day,hour,min,sec,mls))
