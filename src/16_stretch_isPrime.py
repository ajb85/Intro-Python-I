import sys
import math

def isPrime(num):
    sqrt = math.ceil(num**(0.5))
    # Optimization: only have to check to the square root of the number
    for i in range(2, sqrt+1):
        # If num is evenly divisible, it is not prime
        if num % i is 0:
            return False
    return True

def sieve(num):
    # Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
    # Initially, let p equal 2, the smallest prime number.
    # Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list 
        # (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
    # Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, 
        # let p now equal this new number (which is the next prime), and repeat from step 3.
    # When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.
    def removePrimeMultiples(p):
        i = 2
        while(i*p <= num):
            if i*p in integers:
                integers.remove(int(i*p))
            i += 1

    integers = [int(x) for x in range(3, num+1, 2)]

    for i in integers:
        removePrimeMultiples(i)
        


    return integers

# If no argument is supplied, set the num to zero
num = int(sys.argv[1]) if len(sys.argv) > 1 else 0

if num is 0:
    print("Please provide a number greater than 0 to check")
elif num is 1 or num is 2: 
    print(True)
else:
    print(isPrime(num))
    print(sieve(num))




