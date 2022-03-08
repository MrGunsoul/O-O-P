import cat, dog, ferret

def main():
    kitty=cat.Cat("1","Cat","Cindy","2x5m",3000, "meow", "fish", "Mrs",True, 9)
    fretti=ferret.Ferret("2","Ferret","Fred","1x5m",3000, "chortle", "fish", "Mr",True, 5)
    leevi=dog.Dog("3","Husky","Moon Moon","3x5m",3000, "woof", "cow", "Mr",True, "50cm")


    print(leevi)
    leevi.touchy()
main()