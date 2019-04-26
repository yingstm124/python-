#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 06
# Problem 1
# 204111 Sec 003

def main():
	x = float(input(""))
	y = int(input(""))
	print(int_power(x,y))



def int_power(x,y):
	if y<0 :
		i = 0
		power = 1
		while i < abs(y):
			power = power * 1/(x)
			i = i+1
	else:
		i = 0
		power = 1
		while i < abs(y):
			power = power*x
			i = i+1
	return power



if __name__=="__main__":
	main()
	
	

