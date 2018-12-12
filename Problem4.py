#Problem 4 : Commas in Numbers

N=[]        #Empty list
n=int(input("Enter no.of inputs:"))

for i in range(n) :
    a=int(input())
    N.append(a)

for i in N :
    A=[]
    while i>0 :
        a=i//1000
        b=i%1000
        A.append(b)
        i=a
    l=len(A)
    for i in range(l-1,-1,-1) :
        if(i==0) :
            print(A[i],end=" ")
        else :
            print(A[i],end=",")
    print(" ")
            
    
    
