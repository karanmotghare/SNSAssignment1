import sys

def get_euc_coeff(a,b):
    
    if(b==0):
        
        return a,1,0

    g , x0 , y0 = get_euc_coeff(b,a%b)

    y = x0-(a//b)*y0

    x = y0

    return g,x,y

def main():
    
    ip = sys.argv[1:]
    
    a=int(ip[0])
    
    b=int(ip[1])
    
    g,x,y = get_euc_coeff(a,b)

    print(x,end=" ")
     
    print(y,end=" ")


if __name__ == '__main__':
    
    main()
