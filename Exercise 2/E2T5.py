gradeList=[]
def students():
    name=input("Give name: ")
    try:
        grade=int(input("Give grade: "))
        assert 0 <= grade < 6
        
        gradeList.append(grade)
        user=input("Want to input more students(Y/N): ")
        if user == 'Y':
            students()
        if user == 'N':
            print("Average of grades is: ",sum(gradeList)/len(gradeList))
    except AssertionError:
        print("Give number between 0 and 5")
    except ValueError:
        print("Must give a number")



students()