def main():
    print("Input student grades with this format: ", end="")
    print("\'Student ID;Grade1, Grade2, ..., GradeN\': ")
    grades_str = input()
    student_id, gpa_major = compute_major_gpa(grades_str)
    print("Student ID = %s, Major G.P.A. = %.2f" %(student_id, gpa_major))

def compute_major_gpa(grades_str):
    try:
        lst_ = grades_str.split(";")
        student_id = lst_[0]

        grade_lst = lst_[1].split(",")
        grade_lst1 = [grade.upper() for grade in grade_lst]

        ## check grade ##
        for i in grade_lst1:
            if i == "A" or i == "B" or i == "B+" or i == "C" or i == "C+" or i == "D" or i == "D+" or i == "F":
                return
        
        ## check student id ##
        student_id = int(student_id)

        print(grade_lst1)
        grade_d = {"A":4,"B+":3.5,"B":3,"C+":2.5,"C":2,"D+":1.5,"D":1,"F":0}

        
        sum_ = 0
        for grade in grade_lst1:
            for g in grade_d:
                if grade == g:
                    multi = grade_d[g]*3
                    sum_ += multi
                    
        GPA = sum_/(3*len(grade_lst1))
        
        return student_id,GPA
    except ValueError:
        print("Value Error")

if __name__ == "__main__":
    main()