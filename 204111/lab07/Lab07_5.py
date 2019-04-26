def main():
	num = int(input())
	pos = int(input())
	print(rotate(num, pos))


def rotate(num, pos):
	
	check = int(len(str(num)))
	if pos>0:
   #### keep right ######  
		while pos > 0:
		    backnum = (num%10)//1
		    backnum = backnum*10**(check-1)
		    anothernum = num//10
		    num = backnum+anothernum
		    pos -= 1
	else:
	#### keep left #####
		while pos< 0:
			frontnum = num//10**(check-1)
			anothernum = (num%(10**(check-1)))*10
			num = anothernum+frontnum
			pos +=1
			


	return num

if __name__=="__main__":
	main()

