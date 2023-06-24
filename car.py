class Car:
    def __init__(self):
        self.__petrol_in_tank = 0
        self.__odometer_reading = 0

    def fill_up(self):
        self.__petrol_in_tank = 60

    def drive(self, km: int):
        self.__odometer_reading += min(km, self.__petrol_in_tank)
        self.__petrol_in_tank -= min(km, self.__petrol_in_tank)

    def __str__(self):
        return f"Car: odometer reading {self.__odometer_reading} km, " \
            f"petrol remaining {self.__petrol_in_tank} litres"


if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)
    car.fill_up()
    car.drive(10)
    print(car)
