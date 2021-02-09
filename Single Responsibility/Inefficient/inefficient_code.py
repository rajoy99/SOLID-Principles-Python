# This program calculates the binomial distribution for the case of "at most " probability 
# For example : A fair coin is tossed 5000 times. What is the probability that:
# there will be at most 2550 heads?


import math


def atmost(p,n,s):

    """
    returns the at most probability of a binomial distribution 

     arguments:
    p= probability of occurence (type : float )
    n= number of trials (type : integer )
    s= number of specific events (type : integer )
    """

    f=math.factorial

    sum=0
    for i in range(s+1):
        fact=f(n)/(f(i)*f(n-i))
        exact=fact*(p**i)*((1-p)**(n-i))
        sum+=exact
    
    return sum


#  A fair coin is tossed 1000 times. What is the probability that:
# there will be at most 510 heads?
print(atmost(0.5,1000,510))