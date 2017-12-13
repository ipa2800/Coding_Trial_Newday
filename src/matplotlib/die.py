from random import randint

class die():

    def __init__(self,number_side=6):
        self.numbers_side=number_side

    def die_it(self):
        return randint(1,self.numbers_side)
