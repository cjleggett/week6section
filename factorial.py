from cs50 import get_int

def fact1(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

def fact2(n):
    if n == 0:
        return 1
    return n * fact2(n-1)

def fact3(n):
    return 1 if n == 0 else n * fact3(n-1)

def main():
    n = get_int("N: ")
    print(fact1(n))
    print(fact2(n))
    print(fact3(n))

main()