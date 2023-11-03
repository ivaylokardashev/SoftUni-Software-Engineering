class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def change_brand(self, new_brand):
        self.__brand = new_brand

    def get_brand(self):
        return self.__brand


car1 = Car("BMW", "E34")
print(car1.get_brand())
print(car1.__dict__)

car1.change_brand("Mercedes")
print(car1.get_brand())
print(car1.__dict__)