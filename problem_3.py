# 
# Solution to Project Euler problem 3
# Copyright (c) Parv Patel. All rights reserved.
# 
# 

# Prime factor of a given number
def primefactor(number):
    try:   
        factors = []
        while number!=1:
            i = 1
            while True:
                i = i+1
                if number%i==0:
                    factors.append(i)
                    number=number/i
                    break 
        print(max(factors)) # largest prime factor of a number
    except:
        print("Input Number!!")


if __name__ == "__main__":  
    number = int(input("Enter Number: "))
    primefactor(number)