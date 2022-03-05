# Nico Kranni
# car.py
# class Car

class Car:
    def __init__(self, make, model, mileage, price, color, max_load, trunk):
        self._make=make
        self._model=model
        self._mileage=mileage
        self._price=price
        self._color=color
        self._max_load=max_load
        self._trunk=trunk

    def __str__(self):
        return "State of the car:\nMake: {0}\nModel: {1}\nMileage: {2}\nPrice: {3}\nColor: {4}\nMax load: {5}\nTrunk size: {6}".format(self._make,self._model,self._mileage,self._price,self._color,self._max_load,self._trunk)
    

    def getMake(self):
        print("Make is: ", self._make)

    def getModel(self):
        print("Model is: ", self._model)

    def getMileage(self):
        print("Mileage is: ", self._mileage)

    def getPrice(self):
        print("Price is: ", self._price)

    def getColor(self):
        print("Color is: ", self._color)

    def getMaxLoad(self):
        print("Maximum load is: ", self._max_load)

    def getTrunk(self):
        print("Trunk size is: ", self._trunk)
    


    def setMake(self):
        self._make=input("Change make: ")

    def setModel(self):
        self._model=input("Change model: ")

    def setMileage(self):
        self._mileage=input("Give new mileage: ")

    def setPrice(self):
        self._price=input("Set new price: ")

    def setColor(self):
        self._color=input("Give new color: ")

    def setMaxLoad(self):
        self._max_load=input("Give max load size: ")

    def setTrunk(self):
        self._trunk=input("Give trunk size: ")
