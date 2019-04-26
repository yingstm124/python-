
def main():
	n = int(input(""))
	print(life_path(n))


def life_path(n):
#### loop 1 ###########
	check = 2
	while check > 1:
	    i =  0
	    sum_ = 0
	#### loop2 get sum front_back_num ####
	    while n>0:
	        front = (n%10**(i+2))//10**(i+1)
	        back = (n%10**(i+1))//10**(i)
	        sumnum = front+back
	        
	        sum_ += sumnum
	        n //= 10
	        i += 1

	###### check base of sum if it is not one get up loop2 #####

	    check = int(len(str(sum_)))
	    if check != 1:
	        n = sum_
	    else:
	        sum_ = sum_
	    

	return sum_


if __name__=="__main__":
	main()




