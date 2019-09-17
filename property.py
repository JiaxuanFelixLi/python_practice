class Alphabet: 
    #property -- 
    def __init__(self, value): 
        self._value = value 
        #pointer

    # getting the values   

    # attribute/method  
    @property
    #decorator
    def value(self): 
        print('Getting value') 
        return self._value 
          
    # setting the values     
    @value.setter 
    def value(self, value): 
        print('Setting value to ' + value) 
        self._value = value 

    # deleting the values 
    @value.deleter 
    def value(self): 
        print('Deleting value') 
        del self._value

# main
if __name__ == '__main__':
    x = Alphabet('Peter') 
    print(x.value) # property
    
    x.value = 'Diesel' #setter
    
    del x.value #deleter