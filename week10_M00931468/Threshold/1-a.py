primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}
teens = set([13, 14, 15, 16, 17, 18, 19, 13, 14, 15])
print(primes - teens) #Output: {2, 3, 5, 37, 7, 11, 23, 29, 31}, remove all elements which is present in teens from primes
print(primes & teens) #Output: {17, 19, 13}, the intersection between primes and teens
print(primes | teens) #Output: {2, 3, 5, 7, 11, 13, 14, 15, 16, 17, 18, 19, 23, 29, 31, 37}, union of primes and teens
print(primes ^ teens) #Output: {2, 3, 5, 7, 11, 14, 15, 16, 18, 23, 29, 31, 37}, return elements in primes and teens, except their intersection

