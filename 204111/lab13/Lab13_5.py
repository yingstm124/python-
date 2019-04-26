def main():
    list_a = [(2, 7, 1.5), (3.2, 2.5, 4.06), (-5.5, -4.5, 2.5), (2, -5.2, 3), (7.2, -2.8, 1.2)]
    print(count_segment(list_a))

    #(Q1,Q2,Q3,Q4)

def count_segment(list_a):

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for i in range (len(list_a)):
        x,y = (list_a[i][0],list_a[i][1])
        x_plus,x_minus = (list_a[i][0]+list_a[i][2],list_a[i][0]-list_a[i][2])
        y_plus,y_minus =(list_a[i][1]+list_a[i][2],list_a[i][1]-list_a[i][2])


        if x<0 or x_plus<0 or x_minus<0:
            if y>0:
                if y_plus>0 and y_minus>0:
                    q2 -= 1
                q2 += 1
            elif y<0:
                if y_plus<0 and y_minus<0:
                    q3 -= 1
                q3 += 1

        if x>0 or x_plus>0 or x_minus>0:
            if y>0:
                if y_plus>0 and y_minus>0:
                    q1 -= 1
                q1 += 1
            elif y<0:
                if y_plus<0 and y_minus<0:
                    q4 -= 1
                q4 += 1

    qua = (q1,q2,q3,q4)


    return qua


if __name__ == '__main__':
    main()