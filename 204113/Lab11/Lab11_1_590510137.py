import pandas as pd
from math import log2

df = pd.read_csv("data1.txt")
df = df.drop("Film",axis=1)
col = df.columns
success = df[col[len(col)-1]]

def find_max_dict(d):
    max_ = 0
    max_k = ""
    for key in d:
        if d[key] >= max_:
            max_ = d[key]
            max_k = key
    return max_k, max_

def entropy(col, df):
    global success
    
    # classify
    data_dict = {}
    for i in range (len(df[col])):
        if df[col][i] not in data_dict:
            data_dict[df[col][i]] = [0,0]

    for i in range (len(df[col])):
        key = df[col][i]
        if success[i] == True:
            data_dict[key][0] += 1
        elif success[i] == False:
            data_dict[key][1] += 1
    
    #print(data_dict)
    
    result = {}
    for key in data_dict:
        p1 = data_dict[key][0]/(data_dict[key][0] + data_dict[key][1])
        p2 = data_dict[key][1]/(data_dict[key][0] + data_dict[key][1])

        if data_dict[key][0] != 0 and data_dict[key][1] != 0:
            var = ((-1)*(p1)*(log2(p1))) - (p2 * (log2(p2)))
            result[key] = var
        else:
            result[key] = 0
    
    return result

def information_gain(column, df):
    # find E
    dict_entropy = entropy(column, df)
    
    # find P
    dict_prop = {}
    for i in range (len(df[column])):
        if df[column][i] not in dict_prop:
            dict_prop[df[column][i]] = 0
    
    total = len(df[column])
    for i in range (len(df[column])):
        dict_prop[df[column][i]] += 1/total

    # 1 - (P)(E) - ...
    result = 1
    for key in dict_entropy:
        cal = dict_prop[key] * dict_entropy[key]
        result -= cal
    return result

def classify(data):
    d = {}
    for i in range (len(data)):
        if data[i] not in d:
            d[data[i]] = ""
    return d

def main():
    global df, col, success

    finish = False
    i = 0
    gain_compare = {}
    for i in range (len(col)-1):
        gain_compare[col[i]] = 0

    i = 0
    decision = []
    while not finish:
        # classify
        # first decision
        if i == 0:
            for i in range (len(col)-1):
                gain = information_gain(col[i], df)
                gain_compare[col[i]] += gain

        max_k , max_ = find_max_dict(gain_compare)
        decision.append(max_k)
        d = {}
        for i in range (len(df[max_k])):
            if df[max_k][i] not in d:
                d[df[max_k][i]] = 0

        print("First factor is {0}".format(decision[0]))
        # sub_data = classify(df[max_k])
        # df = df.drop(max_k, axis=1)
        # col = df.columns

        # # update new gain_compare
        # gain_compare = {}
        # for i in range (len(col)-1):
        #     gain_compare[col[i]] = 0
        
        # # cal information gain
        # for i in range (len(col)-1):
        #     gain = information_gain(col[i], df)
        #     gain_compare[col[i]] += gain
        # print(gain_compare)

        finish = True

if __name__ == "__main__":
    main()
### หมด passion T T