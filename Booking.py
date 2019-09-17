from car import *
from Customer import *
class Booking(object):
    def __init__(self, Customer, location, Car, period):
        self._Customer = Customer
        self._Location = location
        self._Car = Car
        self._Period = period
    
    @property
    def booking_fee(self):
        fee = self._Car.get_fee(self._Period)
        return fee
    
    @property
    def location(self):
        return self._Location
    
    @property
    def period(self):
        return self._Period

    def __str__(self):
        return "Booking for:  name - {0} car - {1} period - {2} location - {3} fee - {4} ".format(self._Customer, self._Car, self.period, self.location, self.booking_fee)


if __name__ == '__main__':
    # test #
    customer = Customer('felix', '24', 'NB123123')
    car = SmallCar('Felix', 'Toyota')
    Booking = Booking(customer, 'UNSW', car, 30)
    print(Booking.__str__())

    # test done #