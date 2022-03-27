class Car:
    """Модель автомобиля и её описание"""

    def __init__(self, model, year, cash):
        self.model = model
        self.year = year
        self.cash = cash
        self.odometer = 0

    def description(self, odometer=None):
        if self.year >= 2021:
            print(f'Модель: {self.model}, год выпуска: {self.year}, стоимость: {self.cash}$, пробег: {self.odometer}')
        else:
            self.odometer = odometer
            print(f'Модель: {self.model}, год выпуска: {self.year}, стоимость: {self.cash}$, пробег: {self.odometer}')

    def edit_odometer(self, km):
        self.odometer += km


class Battery:
    """Модель аккумулятора электромобиля"""
    def __init__(self, battery=75):
        self.battery = battery

    def describe_battery(self):
        print(f'Мощность аккумулятора: {self.battery} кВт')


class ElectricCar(Car):
    def __init__(self, model, year, cash):
        super().__init__(model, year, cash)
        self.battery = Battery()


my_electric_car = ElectricCar('Tesla', 2020, 40000)
my_electric_car.description(20000)
my_electric_car.battery.describe_battery()


# my_car = Car('Nissan GT-R Nismo', 2021, 85000)
# my_car.edit_odometer(25000)
# my_car.description()




