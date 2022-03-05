import car, truck, suv

def main():
    used_car=car.Car('BMW',2001,70000,15000,4)

    used_truck=truck.Truck('Toyota', 2002, 40000, 12000, "4WD")

    used_suv=suv.SUV("Volvo", 2000, 30000, 18500, 5)

    print('USED CAR INVENTORY')
    print('==================')

    print('The following car is in inventory')
    print(used_car)
    print()
    print('The following pickup truck is in inventory')
    print(used_truck)

main()