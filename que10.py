import math
import sys


def get_gcd(a, b):

    if b == 0:
        return a

    return get_gcd(b, a % b)


def getPhiVal(m):

    count = 0
    #calculate numbers relatively prime to m
    for i in range(1, m):

        gcd = get_gcd(m, i)

        if gcd == 1:
            count += 1

    return count


def get_prime_factors(m):

    s = set()

    for i in range(2, int(math.sqrt(m))+1):

        while (m % i == 0):

            s.add(i)
            m = m // i

    if (m > 2):
        s.add(m)

    return list(s)


def coprimes(a, b):
    if get_gcd(a, b) == 1:
        return True
    else:
        return False

#get reduced residue modulo set


def getRRSM(m):
    RRSM = []
    for i in range(1, m):
        if coprimes(i, m):
            RRSM.append(i)
    return RRSM

def main():
    #get  and m
    m = int(sys.argv[1])
    
    phi_ = getPhiVal(m)
    num_roots = getPhiVal(phi_)
    divisors = get_prime_factors(phi_)
    rrsm_set = getRRSM(m)

    print(num_roots, end=" ")

    for ele in rrsm_set:

        flag = True

        for div in divisors:

            if (ele**(phi_//div)) % m == 1:
                flag = False

        if flag:
            print(ele, end=" ")
    print('')


if __name__ == '__main__':
    main()
