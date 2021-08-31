import sys


def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)


def get_euc_coeff(a, b):

    if(b == 0):

        return a, 1, 0

    g, x0, y0 = get_euc_coeff(b, a % b)

    y = x0-(a//b)*y0

    x = y0

    return g, x, y

def convert_to_crt(sol):

    for i in range(len(sol)):

        eq = sol[i]

        a = eq[0]

        b = eq[1]
        
        m = eq[2]

        g,a_inv, y = get_euc_coeff(a, m)

        a_inv = (a_inv+m) % m

        sol[i] = (1, b*a_inv, m)

def is_sol(sol):

    for i in range(len(sol)):

        eq = sol[i]

        a = eq[0]
        b = eq[1]
        m = eq[2]
        
        g = gcd(a, m)
        
        if g != 1 or b % g != 0:
            return False

    return True

def is_CRT(m_list):

    for i in range(len(m_list)):

        a = m_list[i]

        for j in range(i+1, len(m_list)):

            b = m_list[j]
            if gcd(a, b) != 1:
                return False

    return True

def main():

    ip = sys.argv[2:]

    sol = []
    
    ml = []

    for x in range(0,len(ip),3):

        a = int(ip[x])
        
        b = int(ip[x+1])

        m = int(ip[x+2])

        sol.append((a,b,m))

        ml.append(m)
    
    if(is_CRT(ml)):
        if(is_sol(sol)):

            print("Y",end=" ")

            convert_to_crt(sol)

            cal_m = 1

            for s in sol:
                cal_m=cal_m*s[2]

            cal_b = []
            cal_a = []

            for s in sol:

                g,x,y=get_euc_coeff(cal_m//s[2],s[2])

                cal_a.append(s[1])
                    
                x = (x+s[2])%s[2]

                cal_b.append(x)
                
            fin=0

            for x in range(len(sol)):

                m = ml[x]
                    
                a = cal_a[x]
                    
                b = cal_b[x]

                fin += (cal_m//m)*a*b
                
            print(fin%cal_m,end=" ")
        
    else:
        print("N",end=" ")

if __name__ == '__main__':
    main()
