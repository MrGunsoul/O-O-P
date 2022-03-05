def grades():
    try:
        grade=int(input("points: "))
        if grade < 60 and grade >= 0:
            print ("Fail")
        if grade <= 71 and grade >= 60:
            print ("Grade: 1")
        if grade <=83 and grade >= 72:
            print ("Grade: 2")
        if grade <= 95 and grade >= 84:
            print ("Grade: 3")
        if grade <= 107 and grade >= 96:
            print ("Grade: 4")
        if grade >= 108:
            print ("Grade: 5")
        if grade < 0 or grade > 120:
            print("points have to be between 0 and 120")
    except ValueError:
        print("Value Error")

grades()