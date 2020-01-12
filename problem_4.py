import numpy as np

nums = np.array(range(100,1000))

palindrome = 0
multi_1 = 0
multi_2 = 0
for num in nums:
    arr = nums*num
    for indx, pali in enumerate(arr):
        if str(pali) == str(pali)[::-1]:
            if palindrome < pali:
                palindrome = pali
                multi_1 = num
                multi_2 = nums[indx]

print(multi_1,' x ', multi_2, ' = ', palindrome)

