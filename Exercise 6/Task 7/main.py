import student, teacher, dog, ferret

def main():

    fretti=ferret.Ferret(1,"Ferret","Fred","1x5m",3000, "chortle", "fish", "Mr", True, 5)
    leevi=dog.Dog(2,"Husky","Leevi","3x5m",3000, "woof", "cow", "Mr",True, "50cm")

    steve=ferret.Ferret(3,"Ferret","Steve","1x5m",3000, "chortle", "fish", "Mrs", True, 5)
    moonMoon=dog.Dog(4,"Husky","Moon Moon","3x5m",3000, "woof", "cow", "Mrs",True, "50cm")

    Mr=student.Student(1, "Nico", 27, 175, 90,30000)
    Mrs=teacher.Teacher(2, "Reina", 28, 166, 45, 0)


    Mr.setPet(leevi)
    Mr.setPet(fretti)
    print(Mr.__repr__())
main()