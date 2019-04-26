
def main():
	x = int(input(""))
	base = input("")
	if base == "":
		print(digit_count(x))
	else:
		base = abs(int(base))
		print(digit_count(x,base))


#def digit_count(x, base):
def digit_count(x, base=10):
	i = 0
	sum_ = 0
	num = abs(x)

	while  num>0 :
	    modulo = (num%base)*10**i
	    sum_ += modulo

	    i += 1
	    num//=base

	
	# print("basenary is %d"%sum_)
	
	# check = int(len(str(sum_)))


	return i

if __name__=="__main__":
	main()



