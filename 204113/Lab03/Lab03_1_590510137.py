#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 01
# Problem 3
# 204113 Sec 001

def main():
    i = 1024
    print(two_power_x(i))

def two_power_x(i):
    if i&(i-1) == 0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()