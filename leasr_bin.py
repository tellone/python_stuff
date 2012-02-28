from allscipy_ import *

class crypto_ob:
    def __init__(self,val1=3488, val2=34):
        self._val2=val2
        print ('all set')

    def set_vals(self,val1, val2):
        self._val1=val1
        self._val2=val2
    def get_vals(self):
        return (self._val1, self._val2)

    def least_bin(self,val1,val2):
        g=1
        val1=a
        val2=b
        while a%2==0 and b%2==0:
           a /= 2
           b /= 2
           g *= 2
        while a !=0:
            while a%2==0:
                a /= 2
            while b%2==0:
                b/=2
            if a >= b:
                a=(a-b)/2
            else:
                b=(b-a)/2
        return g*b

    def latent_paser(self,a,b):
       pass

def main():
    Cry=crypto_ob(11333563,6448)
    Cry.get_gb()

