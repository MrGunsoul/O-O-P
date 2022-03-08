import cat, dog, ferret

def main():
    kitty=cat.Cat("1","Cat","Cindy","2x5m",3000, "meow", "fish", "Mrs", 9)
    fretti=ferret.Ferret("2","Ferret","Fred","1x5m",3000, "chortle", "fish", "Mr", 5)
    leevi=dog.Dog("3","Husky","Moon Moon","3x5m",3000, "bark", "cow", "Mr", "50cm")

    print(kitty)
    print(fretti)
    print(leevi)
main()