'''
 Liskov substitution principle defines that objects of a superclass shall be replaceable with objects of its subclasses without breaking the application

'''

class Bird:



class FlyingBird(Bird):

   def fly():
      raise NotImplementedError


class Eagle(FlyingBird):

   def fly():
      pass

class Chicken(Bird):


'''
In this code , the a new class named "FlyingBird" has been implemented. All birds which would be able to use the fly method will be a subclass of this . 
Birds which cannot fly(i.e. cannot use fly method ) will be a subclass of 'Bird' class 
'''