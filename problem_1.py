nums = 1000
prod = 0

for num in range(nums):
    if num%3==0 or num%5==0:
        prod = prod + num

print(prod)
