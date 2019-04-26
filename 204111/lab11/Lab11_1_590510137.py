#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 11
#problem 1
#204111 Sec 003

def main():
      m1 = input()
      m2 = input()
      print(matrix_mult(m1, m2))

def matrix_mult(m1, m2):
      rows_m1 = len(m1[:])
      rows_m2 = len(m2[:])

      ## colum_m1 ##
      for row in range(rows_m1):
            count = 0
            for colum in range(len(m1[row])):
                  count += 1
            colum_m1 = count

      ## colum_m2 ##
      for row in range(rows_m2):
            count = 0
            for colum in range(len(m2[row])):
                  count += 1
            colum_m2 = count

### check ###
      if colum_m1 == rows_m2:
            ## create zero marix was multipled ##
            lst_ = []
            for row in range(rows_m1):
                  lst = []
                  for colum in range(colum_m2):
                        lst.append(0)
                  lst_.append(lst)

            ## multi matrix ##
            for row_m1 in range(rows_m1):
                  for col_m2 in range(colum_m2):
                        for row_m2 in range(rows_m2):
                              lst_[row_m1][col_m2] += m1[row_m1][row_m2] * m2[row_m2][col_m2]
            return  lst_

      else:
            return None

if __name__ == '__main__':
    main()
