import sys

def check_prime(num):
    if num <= 1:
        return False
    for n in range(2, int(num**0.5)+1):
        if num%n == 0:
            return False
    return True

sys.stdin.readlines()