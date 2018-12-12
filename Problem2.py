#Problem 2 : Print the Abbreviation

n=int(input("Enter no. of inputs : "))
N=[]

for i in range(n) :
    a=input().split(" ")
    s= "".join(e[0] for e in a)
    N.append(s)

print ("Abbreviations :")
for i in N :
    print (i)

    
