# 
# Solution to Project Euler problem 6
# Copyright (c) Parv Patel. All rights reserved.
# 
# algorithm for sieve of eratosthenes was implimted from (https://primes.utm.edu/glossary/page.php?sort=SieveOfEratosthenes)
#


def multiples(num, cap):
    return [num*i for i in range(1,int(cap/num)+1)]

# generate bins for segmented sieve
def genbins(lim):
    size = int(lim**(1/2))
    bins = []
    lastval = 0
    multiple = 1
    while lastval<lim:
        bins.append(range(size*multiple, size*(multiple+1), 1))
        lastval = size*(multiple+1)
        multiple += 1
    return bins


# find primes less than "lim"
def simplesieve(lim):
    candidates = [i for i in range(2, lim+1, 1)]
    primes = []
    while len(candidates)!=0:
        primes.append(candidates[0])
        candidates = sorted(list(set(candidates) - set(multiples(primes[-1], lim))))
    return primes


# segmented sieve eratosthenes (https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html)
def segsieve(pos):
    lim = 1000000
    root = lim**(1/2)
    root_primes = simplesieve(int(root)) # start with primes of sqrt(lim)
    primes = root_primes.copy()
    bins = genbins(lim)
    for bin in bins:
        if len(primes) > pos:
            print(f'Prime at position {pos} is {primes[pos-1]}')
            return 
        candidates = [i for i in bin]
        for rp in root_primes:
            candidates = sorted(list(set(candidates) - set(multiples(rp, max(candidates)))))
        primes += candidates


if __name__ == "__main__":  
    segsieve(10001)
    