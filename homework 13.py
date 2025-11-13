class Car:
    counter = 0
    def __init__(self, brand, year, model):
        self.brand = brand
        self.year = year
        self.model = model
        Car.counter+=1
    def car_info(self):
        print(f'Info about car: brand: {self.brand}, model: {self.model}, year: {self.year}, age: {self.age}, number of cars: {Car.counter}')
    def age_of_car(self):
        self.age = 2025 - self.year
    def total_cars(self):
        print(f'There are {Car.counter} cars in total')
class ElectricCar(Car):
    def __init__(self, brand, year, model, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life
    def battery_info(self):
        print(f'ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი')

car1 = Car("BMW", 1986, "M3")
car1.age_of_car()
car1.car_info()

electro = ElectricCar("BMW", "i4", 2024, 14)
electro.age_of_car() 
electro.car_info()
electro.battery_info()
car1.total_cars()
