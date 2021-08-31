import sys
from math import sqrt,pow


def get_gcd(a, b):

    if b == 0:
        return a

    return get_gcd(b, a % b)


def phi_val(m):

    count = 0
    
    for i in range(1, m):

        gcd = get_gcd(m, i)

        if gcd == 1:
            count += 1

    return count

def is_prime(n):

    if(n > 1):

        for x in range(2, int(sqrt(n))+1):

            if(n % x == 0):

                return False

        return True

    else:
        return False



ip = sys.argv[1:]

a = int(ip[0])

x = int(ip[1])

n = int(ip[2])

z=x

if(is_prime(n)):
    
    q = n-1

    x %= q

    print(f"pow({a},{z})(mod {n} ) = pow({a},{x})(mod {n} ) * pow({a},({q}*{z//q})(mod {n} ))")

    print(f"pow({a},{z})(mod {n} ) = pow({a},{x})(mod {n} ) * 1")

    print(f"1. pow({a},{x})(mod {n})")

    print ((a**x)%n)

else:

    q = phi_val(n)

    x %= q

    print(f"pow({a},{z})(mod {n} ) = pow({a},{x})(mod {n} ) * pow({a},({q}*{z//q})(mod {n} ))")

    print(f"pow({a},{z})(mod {n} ) = pow({a},{x})(mod {n} ) * 1")

    print(f"1. pow({a},{x})(mod {n})")

    print((a**x) % n)

