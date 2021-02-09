
'''
To make compliant with Open Closed principle, we would add a new class that will extend
the Automobile Class.  In this new class, we would implement its new behavior
'''

class Automobile:
    def __init__(self, condition, fresh_price):
        self.condition = condition
        self.fresh_price = fresh_price

    def calculate_selling_price(self):
            return self.fresh_price * 0.2


class Old_Automobile(Automobile):
    def calculate_selling_price(self):
        return super().calculate_selling_price() * 2

"""
For a new class of automobile (for example : 'Moderately_old_automobile')  the code can be extended without modifying
Like below :

"""

class Moderately_Old_Automobile(Old):
    def calculate_selling_price(self):
        return super().calculate_selling_price() * 2






