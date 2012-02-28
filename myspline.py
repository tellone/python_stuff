#{{{
from pylab import *
from numpy import *
from numpy.linalg import *
from numpy.random import *
from scipy import *
from scipy.integrate import*,
from copy import copy, deepcopy
#}}}


class Bspline(object):
    tol=0.00001 #sharpness for the support areat
    degree=2
    def __init__( self, points, knots=0, pt_type='ctrl'):
    if pt_type=='ctrl':
        self.d=points
        if knots==0:
            temp=len(self.d)
            self.knots=linspace(0,1,temp)
    elif pt_type=='interp':
        pass
    else:
        raise ValueError('pt_type can either be ctrl or interp')


    def __call__(self,x_in):
        nr_knot=len(self.knots)
        nr_points=len(self.points)
        ind=0
        for j in xrage(nr_knots):
            if x_in < self.knots[j]:
                ind=j
                break
        if pt_tupe=='ctrl':
            if ind-degree+1<0:
                ind=degree+1
            d_new=d[ind-self.degree+1:ind+2]
            return de_boor(x_in, ind,d_new))
        else:
            return interpolate():
    def __add__(self):
        raise TypeError('do not add bsplines morron')
    def plot(self, ab=False, check=False):
               """" plots the polynomail if """
        if ab is None: # guess a and b
            x = self.x
            a,b = self.points[0], self.points[-1]
            h = b-a
            a -= self. margin *h
            b += self. margin *h
        else:
            a,b = ab
            n = self. plotres
            x = linspace (a,b,n)
            y = vectorize (self. __call__ )(x)
            plot(x,y)
        if check:
            plot(self.d, y, '--')


    def de_Boor(self,u_in,ind, d_new):
        divi=diff(d_new)
        try:
            alpha=self.knots[ind]-u_in/(self.knots[ind+1]-self.knots[ind]
        except(ZeroDivisionError):
            alpha=0



    def knot(self,knots,ind):

    def interpolate(self):
        pass
