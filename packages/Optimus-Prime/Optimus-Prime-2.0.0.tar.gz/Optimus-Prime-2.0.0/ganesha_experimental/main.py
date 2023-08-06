import random


def isPrime(n):
    """Validates prime numbers"""
    # Corner case
    if n <= 1:
        return False

    # check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# Function to print primes
def printPrime(n):
    """Takes an input as a number and prints all Prime numbers that come before it printPrime(number)"""
    previous_primes_nb = []
    for i in range(2, n + 1):
        if isPrime(i):
            previous_primes_nb.append(i)
    return previous_primes_nb


def Prime():
    """Takes a number between 2, 100 and prints all Prime numbers before it"""
    n = random.randint(2, 100)
    Prime = str(printPrime(n))[1:-1]
    print(Prime)


if __name__ == "__main__":
    Prime()
