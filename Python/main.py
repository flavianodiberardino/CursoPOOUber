from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola mundo")
    car = Car("AMS123", Account("Andres Herrera", "AND123"))
    print(vars(car))
    print(vars(car.driver))