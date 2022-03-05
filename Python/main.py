from account import Account
from car import Car

def run():
    car = Car("BEF1237", Account("Tony Becera", "KJG3245"))
    print(vars(car))
    print(vars(car.driver))

if __name__ == '__main__':
    run()