#!/usr/bin/env python
'''
Simple simulation of an unidimensional random walk.

  (env) $ pip install scipy numpy
  (env) $ python rw.py 5 100000

For more informations, see <http://mathworld.wolfram.com/RandomWalk1-Dimensional.html>.
'''
import sys

from numpy import random
from scipy.misc import factorial2


def extract_a(N):
    '''
    The variable a follows a binomial distribution, the first time I wrote this,
    I used a uniform distribution and I screwed up the results!
    '''
    return random.binomial(N, 0.5)

def calculate_distance(a, N):
    return 2*a - N

def calculate_theoretical_average(N):
    return factorial2(N - 1, exact=True)/float(factorial2(N - 2, exact=True)) if N % 2 == 0 else factorial2(N, exact=True)/float(factorial2(N - 1, exact=True))


if __name__ == '__main__':

    N           = int(sys.argv[1])
    n_iteration = int(sys.argv[2])

    distances = []

    for _ in xrange(n_iteration):
        a = extract_a(N)

        distance = calculate_distance(a, N)
        distances.append(abs(distance))
        #print a, distance

    total = sum(distances)

    print 'stimated: %.03f theoretical: %.03f'% (
        total/float(len(distances)),
        calculate_theoretical_average(N),
    )
