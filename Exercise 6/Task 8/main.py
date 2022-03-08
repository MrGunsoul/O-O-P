import fish, bird

def main():

    bird1=bird.Bird(1, "V.gryphus", "Andean Condor", 15, "carcasses", False, 3.3)
    fish1=fish.Fish(2,"C. carcharias", "Great White Shark", 2200, "fish", False, 1200)

    print(fish1.storage)
    print(bird1.storage)
main()