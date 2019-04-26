#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 06
# Problem 4
# 204111 Sec 003

total = float(input("Total students: "))
i = 1
sum_ = 0
max_ = 0
run_ = 0

print("Enter score: ")
while i <= total :

    score = float(input(""))
    if score > max_ :
     	run_ = max_
     	max_ = score
        #check = run_
     
    ### score < max_ ####
    elif score>run_ and score < max_ :
       	run_ = score

    ### score < run_   ###
    #elif score<run_:
    	#run_ = score
    
    sum_ = sum_+score
    i += 1

    ###  average  ####
    ave = (sum_)/total

####  check   ########



if run_ ==0: ## check None ###
    print("---\nMax score is: %.2f\nRunner up is: None\nAverage is: %.2f"%(max_,ave))
else:
    print("---\nMax score is: %.2f\nRunner up is: %.2f\nAverage is: %.2f"%(max_,run_,ave))
