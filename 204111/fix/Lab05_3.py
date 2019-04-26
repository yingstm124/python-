def main():
	d = int(input())
	m = int(input())
	y = int(input())
	print(count_down_to_songkran(d, m, y))


def count_down_to_songkran(d, m, y):
    if m == 1:
        day = 103-d
    elif m == 2:
    	day = 72-d
    elif m == 3:
        day = 44-d
    elif m == 4:
        if d <= 13:
            day = 13-d
        else:
            day = 365-(15-d)
    elif m == 5:
        day = 365-(17+d)
    elif m == 6:
        day = 365-(48+d)
    elif m == 7:
        day = 365-(78+d)
    elif m == 8:
        day = 365-(109+d)
    elif m == 9:
        day = 365-(140+d)
    elif m == 10:
        day = 365-(170+d)
    elif m == 11:
        day = 365-(201+d)
    elif m == 12:
        day = 365-(231+d)

    
### check leapyears ####

	##### check after 13 on april #### 
    
    if m>=4 and d>13:
        y = y+1
    elif m>4 :
        y = y+1
    else:
        y = y
      
    ### check leap years #####
    if m==3 or (m==4 and d<=13):
        return day
    
    k = y%4
    p = y%100
    y = y%400
    if(k ==0 and p == 0 and y!=0):
        day = day
    elif(k==0 and y==0):
        day += 1
    elif(k==0 and p!=0):
        day += 1
    elif(k == 0):
        day += 1
    elif(k != 0):
        day = day
    else:
        day = day


        
    return day


if __name__=="__main__":
	main()
