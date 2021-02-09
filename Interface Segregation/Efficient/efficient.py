
class Insect:

    def __init__(scientic_name,size):
        self.scientic_name=scientic_name
        self.size=size

    def walk():
        raise NotImplemented
    
class Ant(Insect):

    def walk():
        pass


    def bite():
        pass
    


class Cockroach(Insect):

    def walk():
        pass

    def fly():
        pass

''' 

The following code abides by Interface segregation principle, by not forcing to depend on methods that would not be used 
In the efficient code Ant class needed to implement fly method which it would not use.
In this code the method fly has been removed from Insect class. 

''' 