'''
How this code solves the problems of the previous code : .
In the inefficient code , all steps were done inside a single function , 
In the restructured code , each function does only one thing. The task of calculating nCr 
and exact probability of specific events have been assigned to two different functions : 
1 ) ncr(n,r) which calculates the nCr which is number of ways in which we can
    choose r objects  
    out of  n objects the order of selection does not matter.
2 ) exactly(p,n,s) which calculates the  exact probability of number 
    of specific events in a  Binomial distribution

Thus dividing the whole task among  several functions contributes 
to the "Reusability " of  the code . 
Testing each functions separately and debugging the code has become a lot easier .
Furthermore ,the code has become organized which makes it very easy to read 
and understand. 

'''
# This program calculates the  probability for the case of "at most " number of specific events
#  in a binomial distribution. 
# For example : A fair coin is tossed 5000 times. What is the probability that:
# there will be at most 2550 heads?


import math

def ncr(n,r):


    '''
    returns  nCr which is the  number of ways in which we can choose r objects  
    out of  n objects the order of selection does not matter.
    arguments : 
    n=  (type : int)
    r=  (type : int)
    '''

    f=math.factorial

    return f(n)/(f(r)*f(n-r))


def exactly(p,n,s):



    '''
    returns the exact probability of a Binomial distribution 

    arguments:
    p= probability of occurence (type : float )
    n= number of trials (type : integer )
    s= number of specific events (type : integer )
    '''


    return ncr(n,s)*(p**s)*((1-p)**(n-s))


def atmost(p,n,s):

    """
    returns the at most probability of a binomial distribution 

     arguments:
    p= probability of occurence (type : float )
    n= number of trials (type : integer )
    s= number of specific events (type : integer )
    """


    sum=0
    for i in range(s+1):
        sum+=exactly(p,n,i)
    
    return sum


#  A fair coin is tossed 1000 times. What is the probability that:
# there will be at most 510 heads?
print(atmost(0.5,1000,510))