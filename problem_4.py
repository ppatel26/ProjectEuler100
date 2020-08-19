# 
# Solution to Project Euler problem 4
# Copyright (c) Parv Patel. All rights reserved.
# 
# 

import numpy as np

def largest_palindrome():
    nums = np.array(range(100,1000))

    palindrome = 0
    multi_1 = 0
    multi_2 = 0
    for num in nums: # loops all values from 100-999 
        arr = nums*num  # multiply each 3-digit number with the full 3-digit sample space
        for indx, pali in enumerate(arr):
            if str(pali) == str(pali)[::-1]:
                if palindrome < pali:
                    palindrome = pali
                    multi_1 = num
                    multi_2 = nums[indx]

    print(multi_1,' x ', multi_2, ' = ', palindrome)

if __name__ == "__main__":  
    largest_palindrome()