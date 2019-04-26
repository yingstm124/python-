def main():
	n = int(input())
	triangle(n)


def triangle(n):

	for a in range (1,n-1):
		if a==1:
			print("*")

		print("*",end="")
		for b in range(2,2*a+1):
			print(".",end="")

		print("*")		

	### last line  #####
	for c in range(n):	
		print("* ",end="")
 



if __name__=="__main__":
	main()
	