#Problem 3 : GCD of 2 numbers

def gcd(a,b) :
    while b!=0 :
        temp=b
        b=a%b
        a=temp
    return a

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

print("GCD of a & b = ",gcd(a,b))
