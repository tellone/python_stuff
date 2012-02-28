#!/bin/env python

"""
File: primes.py
Purpose: calculate all primenumbers between n and 2
Created: 2012-01-27
Maintainer: tellone
Email: filip.diloom@gmail.com
"""

import math
sqrt = math.sqrt
log = math.log
floor = math.floor
from mypoly import
class MyPrimes(object):
    """class for claculating primes"""

    def __call__(self, t_reps, cut_starts, cut_stops):
        """call method for the prime class checks how big the parameters are then
        calls the correct algorithm and print for each run"""

        smaller_p=0
        for rep_nr in t_reps:
            cut_start = cut_starts[rep_nr]
            cut_stop = cut_stops[rep_nr] + 1
            if cut_stop < 400:
                return self.all_primes(cut_stop)
            elif rep_nr == 1:
                smaller_p = self.all_primes(cut_start)
                print self.ask_algorithm(cut_start, cut_stop, smaller_p)

    def bincoff(self, deg_n, deg_k):
        """coeffs of the polynomail (x + 1)^n"""
        return math.factorial(deg_n) // (math.factorial(deg_k) * math.factorial(deg_n - deg_k))

    def is_power(self, un_nr, smaller_p):
        '''check if un_nr is a power of som integer in smaller_p'''

        if un_nr % 2 == 0:
            return True

        first_limit = math.ceil(sqrt(un_nr))
        for c_prime in smaller_p:
            float_p = float(c_prime)
            if c_prime > first_limit:
                return False
            for integ in range(2, 400):
                new_power = float_p ** integ
                if new_power > un_nr:
                    break
                elif un_nr == new_power:
                    return True
        raise AssertionError("this was not supose to go this far")

    def gcd_found(self, int1_in, int2_in) :
        """calcualting greates common divider reurn one if ther is none"""
        int1, int2 = int1_in, int2_in
        while int2 != 0 :
            int1, int2 = int2, int1 % int2
        return int1


    def all_primes(self, cut_stop):
        """finding all primes between n and 2"""
        pr_nr = [2]
        count = 1
        for current in range(3, cut_stop, 2):
            soft_limit = (current + 1) / 2
            for step in range(count) :
                if current % pr_nr[step] == 0:
                    break
                elif pr_nr[step] >= soft_limit:
                    count += 1
                    pr_nr.append(current)
                    break
        return pr_nr


    def ask_algorithm(self, cut_starts, cut_stop, smaller_p):
        '''implementing the ASK mod alogrithm'''

        for current in range(4000, cut_stop, 2):
            #check if current is an even power of another prime
            if self.is_power(current, smaller_p):
                continue
            limiter = floor(log(current, 2))
            #find a new limiter for the next step
            for new_lim in range(1, limiter + 1):
                if current % new_lim == 1:
                    continue
                limiter = new_lim
            for in_common in range(2, limiter + 1):
                c_gcd = self.gcd_found(in_common, current)
                if c_gcd != 1:
                    continue
            for last_step in range(math.ceil(sqrt(limiter)) * log(current, 2)):
                pass

if __name__ == "__main__":
    myP=MyPrimes()
    print myP.gcd_found(5, 55)
    #find_them_faster(1, 5000, 6000)
