import pandas as pd
from math import log2

df = pd.read_csv("data1.txt")
ls_ = df.columns

def entropy(data, success):
    # data
    d = {}
    for i in data:
        if i not in d.keys():
            d[i] = [0,0]
    # [True,False]
    if len(data) == len(success):
        counting = 0
        for i in range (len(data)):
            print("data {0}".format(data[i]))
            if  success[i] == True:
                d[data[i]][0] += 1
            elif success[i] == False:
                d[data[i]][1] += 1
            counting += 1

    # calculattion
    en_d = {}
    for key in d:
        p1 = (d[key][0]/(d[key][0] + d[key][1]))
        p2 = (d[key][1]/(d[key][0] + d[key][1]))
    
        if d[key][0] != 0 and d[key][1] != 0:
            result = ((-1)*(p1)*(log2(p1))) - (p2 * (log2(p2)))
            #result = round(result, 2)
            en_d[key] = result
        else:
            en_d[key] = 0

    return en_d

def information_gain(e_dict, data, column):
    # find property
    # create dict property first
    p_dict = {}
    for key in e_dict:
        p_dict[key] = 0 

    total = 0
    for i in range (len(data)):
        for key in p_dict:
            if key == data[column][i]:
                p_dict[key] += 1
        total += 1

    # calculate property
    for key in p_dict:
        p_dict[key] = p_dict[key]/total
    
    # calculate information gain
    # 1 - (p)(e)
    if len(p_dict) == len(e_dict):
        result = 1
        for key in p_dict:
            cal =  p_dict[key] * e_dict[key]
            #cal = round(cal, 2)
            result -= cal
    
    return result

def factor_list(decision):
    global df

    if len(decision) == 0:
        return  

    # find max ["key", value]
    if len(decision) == 3:
        max_ = [0,0]
        for key in decision:
            if decision[key] >= max_[1]:
                max_[0] = key
                max_[1] = decision[key]

        print("First factor is {0}".format(max_[0]))
       
        factor_list(decision)
    else:
        entropy_d = entropy(df[]) 
        
    


        
# main
decision = {}
#print(len(ls_))
for i in range (1,len(ls_)):
    data = df[ls_]
    if i <= len(ls_)-2:
        column = ls_[i]
        uni_data = df[ls_[i]]
        success = df[ls_[len(ls_)-1]]
        d_entropy = entropy(uni_data, success)
        gain = information_gain(d_entropy, data, column)
        decision[ls_[i]] = gain

factor_list(decision)

# find first decision
# function(df[decision]) find 