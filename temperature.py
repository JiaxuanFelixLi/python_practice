class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
class Celsius1:
    #self(pointer) -- > current class
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self.temperature

    def set_temperature(self, temperature):
        if temperature < -273:
            print("Temperature below -273 is not possible")
        self.temperature = temperature

if __name__ == '__main__':
    man = Celsius()
    man.temperature = 37
    print(man.temperature)
    print(man.to_fahrenheit())
    man = Celsius1(-277)
    man = Celsius1(-200)
    print(man.get_temperature())