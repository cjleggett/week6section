from cs50 import get_int
import time

# This is a very naive function, you can do better!
# Try testing out the running times for some bigger numbers, like 62710561 (not prime), 7919 (prime), 65537 (prime), or 10485985537 (not prime)
def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = get_int("N: ")
    t1 = time.time()
    print("prime" if check_prime(n) else "not prime")
    t2 = time.time()
    print(f"Time elapsed: {t2 - t1} seconds")

main()