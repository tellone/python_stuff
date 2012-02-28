#{{{
from pylab import *
from numpy import *
from numpy.linalg import *
from numpy.random import *
from scipy import *
from scipy.integrate import*
from copy import copy, deepcopy
#}}}
from mypoly import *
p = Polynomial ( points =[(1,0) ,(2,3) ,(3,8), (4,10)])
z = Polynomial ( points =[(1,3) ,(3,20) ,(5,55)])
a=p+z
print a(5)/(z(5)+p(5))

del p,z,a

p=NewtonPolynomial(points =[(1,0) ,(2,3) ,(3,8), (4,10)])
z =NewtonPolynomial ( points =[(1,3) ,(3,20) ,(5,55)])
print z(5)
a=z+p

