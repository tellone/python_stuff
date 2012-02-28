"imports"#{{{
from pylab import *
from numpy import *
from numpy.linalg import *
from numpy.random import *
from scipy import *
from scipy.integrate import *
from copy import copy, deepcopy
#}}}

class Polynomial(object):#{{{
    """Creates a monomial polynomial object """

    base= 'monomial' #keeping track of base with p.base
    def __init__(self,**args):
        """ Constructor take a dictionary **args with a key either points or
        coeff otherwise it returns 1"""
        if args.has_key('points'):
            self.points = array(args['points'])
            self.degree = len(self.points)-1
            self.xi = self.x
            self.coeff = self.point_2_coeff()
        elif args.has_key('coeff'):
            self.coeff = array(args['coeff'])
            self.degree = len(self.coeff)-1
            self.points = self.coeff_2_point()
        else:
            self.coeff = array([[0 , 0]])
            self.xi=array([1.])
            self.points = self.coeff_2_point()
            self.degree = 0
    def point_2_coeff (self):
        """takes the point list and returns the coeff vector """
        return solve ( vander (self.x),self.y)
    def coeff_2_point (self):
        """takes the coeff vector and returns the coeff list"""
        return array ([[x,self(x)] for x in linspace (0,1,len(self.coeff ))])
    @property
    def x(self):
        """decorator for getting x"""
        return self. points [:,0]
    @property
    def y(self):
        """decorator for getting y"""
        return self. points [:,1]
    def zeros(self):
        """returns the companion matrix of p"""
        companion = self. companion ()
        return eigvals ( companion )

    def __add__ (self,poly2):
        """"for adding to polynomail objects p1+p2"""
        if  self.base != poly2.base:
            raise TypeError("Polynomails must be in the same base")
        nr=max(len(self.coeff),len(poly2.coeff))
        nec=zeros(nr)
        coeffn=0
        if nr==len(self.coeff):
            nec[-len(poly2.coeff):]=poly2.coeff
            coeffn=nec+self.coeff
        else:
            nec[-len(self.coeff):] = self.coeff
            coeffn=nec+poly2.coeff
        return Polynomial(coeff=coeffn)

    margin = .05
    plotres = 500

    def plot(self, ab=None, plotinterp=True):
        """" plots the polynomail if """
        if ab is None: # guess a and b
            x = self.x
            a,b = x.min () ,x.max ()
            h = b-a
            a -= self. margin *h
            b += self. margin *h
        else:
            a,b = ab
            n = self. plotres
            x = linspace (a,b,n)
            y = vectorize (self. __call__ )(x)
            plot(x,y)
        if plotinterp :
            plot(self.x, self.y, 'ro' )

    def __call__(self,x):
        """returns p(x)"""
        return polyval (self.coeff ,x)

    def companion(self):
        """returns the companion matrix"""
        d=self.degree
        comp=eye(d,k=-1)
        comp[0,:] -= self.coeff[1:]/self.coeff[0]
        return comp

    def derivate(self):
        """retruns the coeffs for the drivative"""
        self.coeff -= eye(self.degree,1)
    def same(self,poly2):
        """checks to see if a polynomail is the same as the other"""
        if self.base!=poly2.base:
            print "not even in the same base"
            return False
        elif all(self.coeff)==all(poly2.coeff):
            return True
        else:
            return False
#}}}

class NewtonPolynomial (Polynomial):#{{{
    """creates a Newton deviaded differnce polynomail object"""

    base = 'Newton'
    def __init__ (self , **args):
        """Constructor; if just the coeffs key is given it ask for abscissae
        otherwise it calls the polynoamial constructor"""
        if args. has_key ('coeff'):
            try:
                self.xi = array (args['xi'])
            except KeyError :
                raise ValueError ('Coefficients need to be given together with abscissae values xi')
        super(NewtonPolynomial, self).__init__(** args)
    def __call__ (self ,xin):
        """returns N(x)"""
        # first compute the sequence 1, (x-x_1), (x-x_1)(x-x_2) ,...
        nps = hstack ([1., cumprod (xin-self.xi[:self. degree ])])
        return dot(self.coeff , nps)
    def __add__(self,poly2):
        """adds to Newton polynomail and returns a new newtonpolynomail"""
        if  self.base != poly2.base:
            raise TypeError("Polynomails must be in the same base")
        nmax=max(len(self.coeff),len(poly2.coeff))
        nmin=min(len(self.coeff),len(poly2.coeff))
        nec=zeros(nmax)
        coeff2=0
        abi=0
        if nmax==len(self.coeff):
            abi=self.xi
            nec[-nmin:]=poly2.__changepoints__(abi[:nmin])
            coeff2=nec+self.coeff
        else:
            abi=poly2.xi
            nec[-nmin:]=self.__changepoints__(abi[:nmin])
            coeff2=nec+poly2.coeff

        return NewtonPolynomial(coeff = coeff2, xi = abi)

    def point_2_coeff (self):
        return array (list(self. divdiff ()))
    def divdiff(self):
        """computes the ploynomails coeffs"""
        xi = self.x
        row = self.y

        yield row[0]
        for level in xrange(1, len(xi)):
            row = (row[1 :] - row[: -1])/(xi[level :] - xi[: -level])
            if allclose(row,0):
                self.degree = level-1
                break
            yield row[0]
    def __changepoints__(self,new_xi):
        """changes the interpolation points"""
        n_points=[]
        for i in xrange(len(new_xi)):
            new_y=self.__call__(new_xi[i])
            n_points.append( (new_xi[i], new_y))
        new_poly=NewtonPolynomial(points = n_points)
        return new_poly.coeff
#}}}

class LagrangePolynomial(Polynomial):#{{{
    base = 'Lagrange'
    def __init__ (self , **args):
        """Constructor; Checks that input is points then calls the Poynomial
        constructor"""
        if args. has_key ('coeff'):
            raise ValueError ('Points and only points needed for Lagrangepolynomial')
        super(LaragePolynomial, self).__init__(** args)
    def __call__ (self ,xin):
        """returns N(x)"""
        # first compute the sequence 1, (x-x_1), (x-x_1)(x-x_2) ,...
        nps=xin-self.xi
        return dot(self.coeff , nps)
    def __add__(self,poly2):
        """adds to Newton polynomail and returns a newpolynomail"""
        if  self.base != poly2.base:
            raise TypeError("Polynomails must be in the same base")
        pass

    def point_2_coeff (self):
        return self.cardinalcoeff()
    def cardinalcoeff():
        """computes the ploynomails coeffs"""
        xi = self.x
        row = self.y
        cardcoff=0
        for level in xrange(len(xi)):
            coeffn=xi[i]*ones(len(xi))-xi
            coeffn[i]=1
            cardcoff = cardcoff*coeffn
        return cardcoff*row
#}}}

if __name__=="__main__":
    p = Polynomial ( points =[(1,0) ,(2,3) ,(3,8), (4,10)])
    z = Polynomial ( points =[(1,3) ,(3,20) ,(5,55)])
    a=p+z
    print (a(5)-(z(5)+p(5)))/(z(5)+p(5))

    del p, z, a

    p=NewtonPolynomial(points =[(1,1) ,(2,3) ,(3,8), (4,10)])
    z =NewtonPolynomial ( points =[(1,3) ,(3,20) ,(5,55)])
    a=p+z
    print (a(6)-(z(6)+p(6)))/(z(6)+p(6))




