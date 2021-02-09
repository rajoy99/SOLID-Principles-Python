"interface-segregation principle (ISP) states that no client should be forced to depend on methods it does not use."

class Insect:

    def __init__(scientic_name,size):
        self.scientic_name=scientic_name
        self.size=size

    def bite(self):
        raise NotImplemented
    
    def fly(self):
        raise NotImplemented


class Ant(Insect):

    def bite(self):
        pass

    def fly(self):
        pass

''' 
Here , An ant cannot fly. As the fly method has been prototyped in the super class Insect . It would be forced to do so 

''' 
