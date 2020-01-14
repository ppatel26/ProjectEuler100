u_limit = 100

sum_sqr = sum([i**2 for i in range(1, u_limit+1)])

sqr_sum = sum([i for i in range(1, u_limit+1)])**2

diff = abs(sum_sqr - sqr_sum)
print(diff)

