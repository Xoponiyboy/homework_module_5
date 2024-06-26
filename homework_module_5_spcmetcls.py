class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors

home = House(23) # конструктор
print(home.numberOfFloors)
home.setNewNumberOfFloors(10) # Метод объекта
print(home.numberOfFloors)




