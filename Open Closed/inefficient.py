
class Automobile:
    def __init__(self,condition, fresh_price):
        self.condition=condition
        self.fresh_price = fresh_price

    def calculate_selling_price(self):
            if self.customer == 'very old':
                return self.fresh_price * 0.2
            if self.customer == 'old':
                return self.fresh_price * 0.4

    '''
    this does not abide by Open/Closed principle. If we want to give a new
    kind of category of the automobile (for example almost fresh)
    then a the existing code need to be modified by new logic.

    '''

