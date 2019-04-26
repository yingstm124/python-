def main():
    p1 = [2,0,3,6]
    p2 = [4,5]
    print(multiply_polynomials(p1, p2))

def multiply_polynomials(p1, p2):

    len_poly = (len(p1) + len(p2))-1
    result_ls = [0 for i in range (len_poly)]

    for i in range (len(p1)):
        for j in range (len(p2)):
            result_ls[i+j] += p1[i] * p2[j]   

    return result_ls


if __name__ == "__main__":
    main()