from Booking import Booking
from Customer import *  # you can common this line if you pass the test
from car import *
class CarRentalSystem():
    def __init__(self):
        self._Customer = []
        self._car = []
        self._Booking = []

    def searchCar(self, name = None, model = None):
        pass

    def make_Booking(self, Customer, period, car, location):
        Booking = Booking(Customer, location, car, period)
        self._Booking.append(Booking)
        return Booking

    def get_customer(self, username):
        for i in range(len(self._Customer)):
            if(self._Customer[i].get_Name == username):
                print("find user : {0}".format(username))
                return
        print("Cannot match user : {0}".format(username))

    def add_car(self, car):
        self._car.append(car)

    def add_customer(self, customer):
        self._Customer.append(customer)

if __name__ == '__main__':
    # test # 
    rentalSystem = CarRentalSystem()
    rentalSystem.add_customer(Customer('felix', '24', 'NB123123'))
    print("ADD PASSED")
    rentalSystem.get_customer('felix')
    print("Searching Passed")
    car = PremiumCar('Andy', 'Audi')
    rentalSystem.add_car(car)
    if(rentalSystem._car[0].get_Name() == 'Andy' and rentalSystem._car[0].get_model() == 'Audi'):
        print("Add Car Passed")

    # all passed #