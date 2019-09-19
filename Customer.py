class Customer(object):
    def __init__(self, name, age, license):
        self._name = name
        self._age = age
        self._license = license
    @property
    def get_Name(self):
        return self._name

    # toString()
    def __str__(self):
        return "Customer Name {0}, Customer Age {1}, Driving license {2}".format(self._name, self._age, self._license)

# main function
if __name__ == '__main__':
    # instance : customer
    customer = Customer('felix', '24', 'NB123123')
    customer._name = 'david'
    print(customer.__str__())
    #assert(customer._name == 'felix')