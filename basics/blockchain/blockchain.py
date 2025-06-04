import random
from math import ceil

field = 10**5
t, n = 3, 5
secret = 1234
coefficients = []
shares = []
for i in range(0,t-1):
    coefficients.append(random.randrange(0, field))
coefficients.append(secret)
for i in range(1, n+1):
    value = 0
    k = 0
    for coefficient in coefficients[::-1]:
        value= value+ ((i**k)*coefficient)
        k = k+1
    shares.append((i, value))
print("Shares are:")
for share in shares:
    print(share)

  
pool=random.sample(shares, t)
sums= 0
for share_j in pool:
    xj,yj = share_j[0],share_j[1]
    prod = 1
    for share_i in pool:
        xi,yi=share_i[0],share_i[1]
        if xi != xj:
            prod *= (-xi)/(xj-xi)
    prod*= yj
    sums+=prod
print("Original Secret:", secret)
print("Reconstructed Secret:",int(round(sums,0)))
