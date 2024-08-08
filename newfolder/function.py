# finb
def finb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return finb(n-1) + finb(n-2)


def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def prime(n):
    if n < 2:
        return "Not prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not prime"
    return "Prime"