# 
# Solution to Project Euler problem 2
# Copyright (c) Parv Patel. All rights reserved.
# 
# 

# Create a fib series (<4M)
fib = [1,2]
while fib[-1] < 4e6:
    fib.append(fib[-1]+fib[-2])

# Sum even valued terms
total = 0
for val in fib:
    if val%2==0:
        total = total + val 

print(total)
