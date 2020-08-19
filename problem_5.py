# 
# Solution to Project Euler problem 5
# Copyright (c) Parv Patel. All rights reserved.
# 
# 

# Brute Force Method (Takes too long!) 
'''
num = 1
flag = 0
while True:
    #print(num)
    for i in range(1,u_end+1):
        if num%i==0:
            if i==u_end and num%i==0:
                flag = 1
                break
            continue
        else:
            break
    if flag==1:
        break
    num = num+1

print(num)
'''

# Method-2 (reduce solution space)
def factorial(num):
    facto = 1
    for i in range(1,num+1):
        facto = facto*i
    return facto


# (1 - u_end) : defines range of numbers
def smallest_number_divisible(u_end):
    facto = factorial(u_end)  # start with the factorial of end number (caps the sample space)
    pots = []
    count = u_end
    while count!=0:
        check = all([facto%i==0 for i in range(u_end,0,-1)]) # update the facto=number and check if divisible by all numbers from (1-u_end)
        if check:
            pots.append(facto)
            facto = facto/count
            count = count - 1
        else:
            facto = pots[-1]/count
            count = count - 1
    
    print(min(pots))

if __name__ == "__main__":  
    smallest_number_divisible(20)
