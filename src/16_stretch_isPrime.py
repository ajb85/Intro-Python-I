import sys
import math

def isPrime(num):
    sqrt = math.ceil(int(num)**(0.5))
    # Optimization: only have to check to the square root of the number
    for i in range(2, sqrt+1):
        # If num is evenly divisible, it is not prime
        if int(num) % i is 0:
            return False
    return True

# If no argument is supplied, set the num to zero
num = int(sys.argv[1]) if len(sys.argv) > 1 else 0

if num is 0:
    print("Please provide a number greater than 0 to check")
elif num is 1 or num is 2: 
    print(True)
else:
    print(isPrime(sys.argv[1]))