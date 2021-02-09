class Bird:

    def fly():
        pass 


class Eagle(Bird):

    def fly():
        pass


class Chicken(Bird): 


'''
Eagle is a bird , it should be able to use fly method 

But ,Chicken is also a bird, but it can't fly, Chicken class is a subtype of class Bird, but it shouldn't be able to use the fly method, 
that breaks the LSP principle.

'''
