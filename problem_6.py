# 
# Solution to Project Euler problem 6
# Copyright (c) Parv Patel. All rights reserved.
# 
# 


def sumsqr_sqrsum(u_limit):
    sum_sqr = sum([i**2 for i in range(1, u_limit+1)])  # sum of squares
    sqr_sum = sum([i for i in range(1, u_limit+1)])**2  # square of sums
    diff = abs(sum_sqr - sqr_sum)
    print(diff)

if __name__ == "__main__":  
    sumsqr_sqrsum(100)