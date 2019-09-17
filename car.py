from abc import ABC
class car(ABC):
    def __init__(self, name, model, rate):
        self._name = name
        self._model = model
        self._rate = rate

    def get_Name(self):
        return self._name
    
    def get_model(self):
        return self._model

    def get_fee(self, period):
        return period*self._rate
    
    def __str__(self):
        return "Car details {0}, {1}".format(self._name, self._model)

class SmallCar(car):
    def __init__(self, name, model):
        super().__init__(name, model, 50)

class MediumCar(car):
    def __init__(self, name, model):
        super().__init__(name, model, 75)

class LargeCar(car):
    def __init__(self, name, model):
        super().__init__(name, model, 100)

    def get_fee(self, period):
        if period >= 7:
            fee = fee*0.95
        return fee

class PremiumCar(car):
    def __init__(self, name, model):
        super().__init__(name, model, 150)
        self._premium_tariff = 0.15
    def get_fee(self, period):
        return super().get_fee*1.15


if __name__ == '__main__':

    # test #
    s =SmallCar('felix', 'toyota')
    print(s.get_fee(10))

    m = MediumCar('David', 'Volks')
    print(s.get_fee(15))

    l = LargeCar('Dorothy', 'Benz')
    print(s.get_fee(20))

    p = PremiumCar('Andy', 'Audi')
    print(s.get_fee(25))

    # test Passed # 