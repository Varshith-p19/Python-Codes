
#Find the GCD (greatest common divisor) of two numbers using a loop.

def greatest_comman_divisor(a,b):
    gcd = 1
    
    for i in range(2,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd = i
    print("Greatest Comman Devisor is",gcd)
    
greatest_comman_divisor(12,18)
